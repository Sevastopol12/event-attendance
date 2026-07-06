import reflex as rx
from checkin_app.pages.main.state import MainState, CarouselState

def event_timeline() -> rx.Component:
    """A visual timeline component showing event progress with responsive constraints."""
    return rx.vstack(
        rx.flex(
            # Start Time
            rx.text(
                CarouselState.selected_event_start_time_formatted,
                font_family="Outfit",
                font_weight="600",
                font_size=rx.breakpoints(xs="0.8rem", sm="0.9rem"),
                color=MainState.theme_colors["text_primary"],
            ),
            # End Time
            rx.text(
                CarouselState.selected_event_end_time_formatted,
                font_family="Outfit",
                font_weight="600",
                font_size=rx.breakpoints(xs="0.8rem", sm="0.9rem"),
                color=MainState.theme_colors["text_primary"],
            ),
            justify="between",
            width="100%",
            marginBottom="0.5rem",
        ),
        # Progress bar
        rx.box(
            rx.box(
                width=CarouselState.selected_event_progress_text,
                height=rx.breakpoints(xs="12px", sm="16px"),
                background_color=MainState.theme_colors["aurora_teal"],
                border_radius="20px",
                transition="width 0.5s ease-in-out",
                box_shadow=f"0 0 20px {MainState.theme_colors['aurora_teal']}",
                filter=f"drop-shadow(0 0 8px {MainState.theme_colors['aurora_teal']})",
            ),
            width="100%",
            height=rx.breakpoints(xs="12px", sm="16px"),
            background_color=rx.cond(
                MainState.dark_mode,
                "rgba(255, 255, 255, 0.1)",
                "rgba(0, 0, 0, 0.1)",
            ),
            border_radius="20px",
            overflow="hidden",
        ),
        width="100%",
        align="stretch",
        spacing="2",
        marginTop="1rem",
        marginBottom="0rem",
    )
