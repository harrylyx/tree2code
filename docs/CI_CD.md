# CI/CD 说明

本项目使用 GitHub Actions 做自动测试和自动发布。

## 1. CI（自动测试）

文件：`.github/workflows/ci.yml`

触发条件：
- push 到 `main`
- pull request 到 `main`
- 手动触发

包含两个作业：

1) `test-main`
- Python 3.13
- 启动 PostgreSQL 服务（CI 内部测试账号，通过环境变量注入）
- 跑完整 `pytest`

2) `matrix-smoke`
- Python 3.8 ~ 3.14
- XGBoost / LightGBM 双后端烟测
- 确保跨版本基础可用性

## 2. Release（自动构建与发布 wheel）

文件：`.github/workflows/release.yml`

触发条件：
- push tag（`v*`）
- 手动触发

执行内容：
1. 用 `uv build` 构建 `dist/*.whl` 和 `dist/*.tar.gz`
2. 上传构建产物到 workflow artifacts
3. 自动创建/更新 GitHub Release 并附加构建包

## 3. 使用方式

### 3.1 触发 CI
- 正常提交 PR 即自动触发。

### 3.2 发布新版本

```bash
git tag v0.1.0
git push origin v0.1.0
```

推送 tag 后会自动构建并发布 wheel。

## 4. 备注

- 当前默认发布目标是 GitHub Release（wheel/sdist 产物）。
- 如果后续需要自动发 PyPI，可在此基础上再增加发布步骤和 secret。
