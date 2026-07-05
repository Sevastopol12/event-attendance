import reflex as rx
from checkin_app.pages.main.state import MainState
from checkin_app.styles.visual_system import (
    get_unified_card_styles,
    get_unified_text_styles,
)


def description_card_skeleton() -> rx.Component:
    """Skeleton for the description card."""
    return rx.box(
        rx.vstack(
            # Header Skeleton
            rx.flex(
                rx.skeleton(width="20px", height="20px"),
                rx.skeleton(width="120px", height="0.8rem"),
                align="center",
                spacing="2",
                marginBottom="1rem",
            ),
            # Content Skeleton
            rx.vstack(
                rx.skeleton(width="100%", height="1.1rem"),
                rx.skeleton(width="90%", height="1.1rem"),
                rx.skeleton(width="95%", height="1.1rem"),
                rx.skeleton(width="60%", height="1.1rem"),
                align="start",
                spacing="2",
            ),
            align="start",
            spacing="2",
        ),
        width="100%",
        max_width="800px",
        padding=rx.breakpoints(xs="1.25rem", sm="1.5rem", md="2rem"),
        border_radius="24px",
        **get_unified_card_styles(MainState.dark_mode, MainState.theme_colors),
    )


def description_card() -> rx.Component:
    """A decorated card displaying the event description.

    Matches the glassmorphism and aurora aesthetic of the attendance block.
    """
    actual_card = rx.card(
        rx.vstack(
            # Header
            rx.flex(
                rx.icon("info", size=20, color=MainState.theme_colors["aurora_teal"]),
                rx.text(
                    "Event Description",
                    font_size="0.8rem",
                    font_weight="600",
                    text_transform="uppercase",
                    letter_spacing="0.05em",
                    **get_unified_text_styles(),
                ),
                align="center",
                spacing="2",
                margin_bottom="1rem",
            ),
            # Content
            rx.text(
                MainState.selected_event_description,
                text_align="left",
                font_size=rx.breakpoints(xs="0.95rem", sm="1rem", md="1.1rem"),
                line_height="1.7",
                letter_spacing="0.01em",
                **get_unified_text_styles(),
            ),
            align="start",
            spacing="2",
        ),
        width="100%",
        max_width="800px",
        padding=rx.breakpoints(xs="1.25rem", sm="1.5rem", md="2rem"),
        border_radius="24px",
        variant="ghost",
        **get_unified_card_styles(MainState.dark_mode, MainState.theme_colors),
    )

    return rx.cond(
        MainState.is_data_loaded,
        actual_card,
        description_card_skeleton(),
    )
