#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


PYTHON_SERIES = ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]

XGB_CANDIDATES_DESC = [
    "3.2.0",
    "2.1.4",
    "2.0.3",
    "1.7.6",
    "1.7.0.post0",
    "1.0.2",
    "1.0.0",
]

LGB_CANDIDATES_DESC = [
    "4.6.0",
    "4.5.0",
    "4.4.0",
    "4.3.0",
    "4.0.0",
    "3.3.5",
    "2.3.1",
    "2.0.2",
]


@dataclass
class ProbeResult:
    success: bool
    stdout: str
    stderr: str


def _run(cmd: Sequence[str], cwd: Path) -> ProbeResult:
    proc = subprocess.run(
        list(cmd),
        cwd=str(cwd),
        text=True,
        capture_output=True,
    )
    return ProbeResult(success=(proc.returncode == 0), stdout=proc.stdout, stderr=proc.stderr)


def _find_python(version: str, cwd: Path) -> Optional[str]:
    r = _run(["uv", "python", "find", version], cwd=cwd)
    if not r.success:
        return None
    path = r.stdout.strip()
    return path or None


def _probe_installable(
    python_path: str,
    package: str,
    version: str,
    cwd: Path,
    import_name: str,
) -> bool:
    r = _run(
        [
            "uv",
            "run",
            "--isolated",
            "--python",
            python_path,
            "--with",
            f"{package}=={version}",
            "python",
            "-c",
            f"import {import_name}; print({import_name}.__version__)",
        ],
        cwd=cwd,
    )
    return r.success


def _pick_low_high_versions(
    python_path: str,
    package: str,
    import_name: str,
    candidates_desc: Sequence[str],
    cwd: Path,
) -> Tuple[Optional[str], Optional[str], List[str]]:
    logs: List[str] = []

    high: Optional[str] = None
    for version in candidates_desc:
        ok = _probe_installable(python_path, package, version, cwd, import_name)
        logs.append(f"probe high {package}=={version}: {'ok' if ok else 'fail'}")
        if ok:
            high = version
            break

    low: Optional[str] = None
    for version in reversed(candidates_desc):
        ok = _probe_installable(python_path, package, version, cwd, import_name)
        logs.append(f"probe low {package}=={version}: {'ok' if ok else 'fail'}")
        if ok:
            low = version
            break

    return low, high, logs


def _run_smoke(
    cwd: Path,
    python_path: str,
    backend: str,
    package_spec: str,
) -> ProbeResult:
    return _run(
        [
            "uv",
            "run",
            "--isolated",
            "--python",
            python_path,
            "--with",
            "numpy",
            "--with",
            "pandas",
            "--with",
            "scikit-learn",
            "--with",
            package_spec,
            "python",
            "scripts/matrix_smoke.py",
            "--backend",
            backend,
        ],
        cwd=cwd,
    )


def run_matrix(cwd: Path) -> Dict[str, object]:
    summary: Dict[str, object] = {
        "python_versions": {},
        "notes": [
            "Requested floors: xgboost>=1.0, lightgbm>=2.0",
            "Per Python version: run lowest installable and highest installable.",
        ],
    }

    for py in PYTHON_SERIES:
        py_path = _find_python(py, cwd)
        if py_path is None:
            summary["python_versions"][py] = {
                "status": "skipped",
                "reason": "python_not_found",
            }
            continue

        py_report: Dict[str, object] = {
            "python_path": py_path,
            "status": "ok",
            "logs": [],
            "runs": [],
        }

        xgb_low, xgb_high, xgb_logs = _pick_low_high_versions(
            python_path=py_path,
            package="xgboost",
            import_name="xgboost",
            candidates_desc=XGB_CANDIDATES_DESC,
            cwd=cwd,
        )
        lgb_low, lgb_high, lgb_logs = _pick_low_high_versions(
            python_path=py_path,
            package="lightgbm",
            import_name="lightgbm",
            candidates_desc=LGB_CANDIDATES_DESC,
            cwd=cwd,
        )
        py_report["logs"].extend(xgb_logs)
        py_report["logs"].extend(lgb_logs)

        run_specs: List[Tuple[str, str]] = []
        if xgb_low is not None:
            run_specs.append(("xgboost", f"xgboost=={xgb_low}"))
        if xgb_high is not None and xgb_high != xgb_low:
            run_specs.append(("xgboost", f"xgboost=={xgb_high}"))
        if lgb_low is not None:
            run_specs.append(("lightgbm", f"lightgbm=={lgb_low}"))
        if lgb_high is not None and lgb_high != lgb_low:
            run_specs.append(("lightgbm", f"lightgbm=={lgb_high}"))

        if not run_specs:
            py_report["status"] = "skipped"
            py_report["reason"] = "no_installable_versions"
            summary["python_versions"][py] = py_report
            continue

        for backend, pkg_spec in run_specs:
            smoke = _run_smoke(cwd=cwd, python_path=py_path, backend=backend, package_spec=pkg_spec)
            run_result: Dict[str, object] = {
                "backend": backend,
                "package": pkg_spec,
                "ok": smoke.success,
            }
            if smoke.stdout.strip():
                try:
                    run_result["output"] = json.loads(smoke.stdout.strip().splitlines()[-1])
                except Exception:
                    run_result["output"] = smoke.stdout.strip()
            if not smoke.success:
                run_result["stderr"] = smoke.stderr.strip()
                py_report["status"] = "failed"
            py_report["runs"].append(run_result)

        summary["python_versions"][py] = py_report

    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="matrix_report.json",
        help="Path to save the matrix report JSON",
    )
    args = parser.parse_args()

    cwd = Path(__file__).resolve().parent.parent
    report = run_matrix(cwd)

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = cwd / output_path
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))

    failed = False
    for py_report in report["python_versions"].values():
        if isinstance(py_report, dict) and py_report.get("status") == "failed":
            failed = True
            break

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
