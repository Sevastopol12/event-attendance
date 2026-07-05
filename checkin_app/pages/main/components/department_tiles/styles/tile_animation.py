import reflex as rx

from checkin_app.pages.main.state import MainState
from checkin_app.styles.theme import NORTHERN_LIGHTS_COLORS

teal_dark = NORTHERN_LIGHTS_COLORS["dark"]["aurora_teal"]
teal_light = NORTHERN_LIGHTS_COLORS["light"]["aurora_teal"]
active_color = rx.cond(MainState.dark_mode, teal_dark, teal_light)


def get_tile_base_styles(is_active: bool, is_expired: bool) -> dict:
    """Returns compact, responsive base styles for the tile."""

    return {
        "position": "relative",
        "border_radius": "12px",
        "padding": rx.breakpoints(xs="0.75rem 0.5rem", sm="1rem", md="1.25rem"),
        "height": rx.breakpoints(xs="70px", sm="100px", md="110px"),
        "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
        "cursor": rx.cond(is_expired, "not-allowed", "pointer"),
        "opacity": rx.cond(is_expired, "0.6", "1"),
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "background": rx.cond(
            is_active,
            rx.cond(
                MainState.dark_mode,
                f"radial-gradient(circle at center, {teal_dark}12 0%, #0F172A 100%)",
                f"radial-gradient(circle at center, {teal_light}08 0%, #F1F5F9 100%)",
            ),
            rx.cond(MainState.dark_mode, "#0F172A", "#FFFFFF"),
        ),
        "border": rx.cond(
            is_active,
            rx.cond(
                MainState.dark_mode,
                f"1px solid {active_color}88",
                f"1.5px solid {active_color}",
            ),
            rx.cond(
                MainState.dark_mode,
                "1px solid rgba(30, 41, 59, 0.8)",
                "1px solid rgba(226, 232, 240, 0.8)",
            ),
        ),
        "backdrop_filter": rx.cond(is_active, "blur(8px)", "none"),
        "box_shadow": rx.cond(
            is_active,
            rx.cond(
                MainState.dark_mode,
                f"0 4px 12px {active_color}15",
                f"0 4px 10px rgba(13, 148, 136, 0.08)",
            ),
            "none",
        ),
    }


def get_tile_hover_styles(is_active: bool, is_expired: bool) -> dict:
    """Returns hover styles for the tile."""
    return {
        "transform": rx.cond(
            is_expired,
            "none",
            rx.cond(is_active, "scale(1.02) translateY(-4px)", "translateY(-4px)"),
        ),
        "border": rx.cond(
            is_expired,
            "inherit",
            rx.cond(
                is_active,
                f"1px solid {active_color}BB",
                rx.cond(
                    MainState.dark_mode,
                    "1px solid rgba(71, 85, 105, 0.5)",
                    "1px solid rgba(203, 213, 225, 0.8)",
                ),
            ),
        ),
        "box_shadow": rx.cond(
            is_expired,
            "none",
            rx.cond(
                is_active,
                rx.cond(
                    MainState.dark_mode,
                    f"0 0 40px {active_color}66",
                    f"0 8px 20px rgba(0,0,0,0.15)",
                ),
                "none",
            ),
        ),
    }
