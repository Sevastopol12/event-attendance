import reflex as rx
from checkin_app.pages.main.state import MainState

def status_strip() -> rx.Component:
    """A simplified app bar providing global context and theme control.

    Returns:
        rx.Component: The StatusStrip component.
    """
    return rx.box(
        rx.flex(
            # Left: App Title
            rx.text(
                "Event Attendance",
                font_family="Outfit",
                font_weight="700",
                font_size="1.2rem",
                color=MainState.theme_colors["text_primary"],
            ),
            # Right: Theme Toggle
            rx.flex(
                rx.button(
                    rx.cond(
                        MainState.dark_mode,
                        rx.icon("sun"),
                        rx.icon("moon"),
                    ),
                    on_click=MainState.toggle_dark_mode,
                    variant="ghost",
                    color=MainState.theme_colors["text_primary"],
                    margin_right="1rem",
                    cursor="pointer",
                    background="transparent",
                    _hover={"background": "rgba(255, 255, 255, 0.1)"},
                ),
                align="center",
            ),
            width="100%",
            justify="between",
            align="center",
            padding=rx.breakpoints(xs="0.5rem 1rem", md="0.75rem 1.5rem"),
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="100",
        background_color=rx.cond(
            MainState.dark_mode,
            "rgba(2, 6, 23, 0.8)",
            "rgba(248, 250, 252, 0.8)",
        ),
        backdrop_filter="blur(12px)",
        border_bottom="1px solid rgba(255, 255, 255, 0.15)",
        box_shadow="0 4px 12px rgba(0, 0, 0, 0.3)",
        font_family="Outfit",
    )
