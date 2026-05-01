"""嵐海知識｜品牌資產（LOGO + favicon）"""

from __future__ import annotations
from pathlib import Path
import streamlit as st


ROOT = Path(__file__).resolve().parent.parent
LOGO_PATH = ROOT / "static" / "lanhai-logo.png"


def get_page_icon(fallback_emoji: str) -> str:
    """If LOGO file exists, use it as favicon; else fall back to emoji."""
    return str(LOGO_PATH) if LOGO_PATH.exists() else fallback_emoji


def render_sidebar_logo() -> None:
    """Show the LOGO at the top of every page's sidebar (Streamlit ≥ 1.31)."""
    if LOGO_PATH.exists():
        try:
            st.logo(str(LOGO_PATH), size="large")
        except (TypeError, AttributeError):
            # st.logo() not available or 'size' kwarg not supported
            pass
