"""Minimal package to satisfy Poetry's package discovery.

This package is intentionally minimal — it exists so poetry/installer
can find a package for the project name (normalized with underscores).
It does not change how Streamlit runs `app.py` at the repo root.
"""

__version__ = "0.1.0"
