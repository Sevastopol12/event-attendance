"""
Visual system helper functions for consistent UI styling across the application.
Provides unified styles for cards and text to maintain the aurora glassmorphism aesthetic.
"""

import reflex as rx
from typing import Any

def get_unified_card_styles(dark_mode: Any, theme_colors: dict[str, str]) -> dict[str, Any]:
    """Returns a dictionary of styles for a unified glassmorphism card.

    Args:
        dark_mode: Whether the application is in dark mode (Reflex Var).
        theme_colors: The current theme color palette.

    Returns:
        A dictionary of Reflex style properties.
    """
    return {
        "background_color": rx.cond(
            dark_mode,
            "rgba(15, 23, 42, 0.6)",
            "rgba(255, 255, 255, 0.6)",
        ),
        "backdrop_filter": "blur(16px)",
        "border": rx.cond(
            dark_mode,
            "1px solid rgba(45, 212, 191, 0.3)",
            "1px solid rgba(13, 148, 136, 0.3)",
        ),
        "box_shadow": rx.cond(
            dark_mode,
            "0 8px 32px 0 rgba(0, 0, 0, 0.37)",
            "0 8px 32px 0 rgba(255, 255, 255, 0.2)",
        ),
    }

def get_unified_text_styles() -> dict[str, Any]:
    """Returns a dictionary of styles for unified text elements.

    Returns:
        A dictionary of Reflex style properties.
    """
    return {
        "font_family": "Outfit",
        "transition": "color 0.3s ease",
    }
