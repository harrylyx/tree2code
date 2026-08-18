"""Convert XGBoost and LightGBM models into SQL or Python."""

from .api import convert

__version__ = "0.3.0"

__all__ = ["__version__", "convert"]
