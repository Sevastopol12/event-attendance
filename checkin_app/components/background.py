"""
Animated aurora-inspired background component.
"""

import reflex as rx
from checkin_app.pages.main.state import MainState
from checkin_app.styles.theme import NORTHERN_LIGHTS_COLORS

def aurora_background(*children: rx.Component) -> rx.Component:
    """
    A component that renders an animated background with aurora-like colors.
    Uses CSS animations and blurred elements for an ethereal look.

    Returns:
        rx.Component: The styled background component.
    """
    def create_aurora_blob(color_dark: str, color_light: str, top: str, left: str, width: str, height: str, animation: str) -> rx.Component:
        return rx.box(
            position="absolute",
            top=top,
            left=left,
            width=width,
            height=height,
            background=rx.cond(
                MainState.dark_mode,
                f"radial-gradient(ellipse at center, {color_dark} 0%, transparent 60%)",
                f"radial-gradient(ellipse at center, {color_light} 0%, transparent 60%)",
            ),
            style={
                "filter": "blur(90px)",
                "animation": animation,
                "opacity": rx.cond(MainState.dark_mode, "0.45", "0.65")
            },
            z_index="-1",
            border_radius="50%",
        )

    return rx.box(
        rx.box(
            create_aurora_blob(
                NORTHERN_LIGHTS_COLORS["dark"]["aurora_cyan"],
                NORTHERN_LIGHTS_COLORS["light"]["aurora_cyan"],
                top="-15%", left="-10%", width="70vw", height="70vh",
                animation="aurora_drift_1 22s infinite alternate ease-in-out"
            ),
            create_aurora_blob(
                NORTHERN_LIGHTS_COLORS["dark"]["aurora_green"],
                NORTHERN_LIGHTS_COLORS["light"]["aurora_green"],
                top="40%", left="50%", width="60vw", height="60vh",
                animation="aurora_drift_2 28s infinite alternate ease-in-out"
            ),
            create_aurora_blob(
                NORTHERN_LIGHTS_COLORS["dark"]["aurora_violet"],
                NORTHERN_LIGHTS_COLORS["light"]["aurora_violet"],
                top="15%", left="55%", width="75vw", height="75vh",
                animation="aurora_drift_3 25s infinite alternate ease-in-out"
            ),
            create_aurora_blob(
                NORTHERN_LIGHTS_COLORS["dark"]["aurora_magenta"],
                NORTHERN_LIGHTS_COLORS["light"]["aurora_magenta"],
                top="45%", left="-15%", width="65vw", height="65vh",
                animation="aurora_drift_4 32s infinite alternate ease-in-out"
            ),
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="-1",
            overflow="hidden",
            background_color=rx.cond(
                MainState.dark_mode,
                "#020617", # deep midnight blue
                "#F8FAFC", # light clean background
            ),
        ),
        *children,
        min_height="100vh",
        position="relative",
        overflow_x="hidden",
    )
