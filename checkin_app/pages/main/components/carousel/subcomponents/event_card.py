import reflex as rx

from checkin_app.pages.main.state import MainState, EventItem
from ..styles import CARD_WIDTH_PX


def event_card(event: EventItem) -> rx.Component:
    """A selectable event card."""
    is_active = event.id == MainState.selected_event_id

    # Event time
    time_stack = rx.vstack(
        rx.text(
            event.time,
            color=rx.cond(
                is_active,
                MainState.theme_colors["text_primary"],
                MainState.theme_colors["text_secondary"],
            ),
            font_family="Outfit",
            font_size="1.05rem",
            font_weight="800",
        ),
        rx.box(
            width="10px",
            height="10px",
            border_radius="full",
            background=rx.cond(
                event.status == "Active",
                MainState.theme_colors["aurora_teal"],
                "gray",
            ),
        ),
        width="30%",
        align="center",
        justify="center",
    )

    # Event status
    status_stack = rx.vstack(
        rx.badge(
            event.status,
            color_scheme=rx.cond(
                event.status == "On-going",
                "green",
                rx.cond(event.status == "Expired", "red", "gray"),
            ),
            variant="solid",
            font_size="0.65rem",
            padding="2px 8px",
        ),
        rx.heading(
            event.title,
            size="3",
            color=rx.cond(
                is_active,
                MainState.theme_colors["text_primary"],
                MainState.theme_colors["text_secondary"],
            ),
            font_family="Outfit",
            line_height="1.2",
            font_weight="700",
        ),
        width="70%",
        align="start",
        justify="center",
        padding_left="1rem",
        border_left="1px solid rgba(255, 255, 255, 0.15)",
    )

    # Main component
    return rx.box(
        rx.hstack(
            time_stack,
            status_stack,
            width="100%",
            height="100%",
            spacing="0",
        ),
        id=f"card-{event.id}",
        custom_attrs={"data-id": event.id},
        class_name=rx.cond(
            is_active,
            "event-card event-card-active event-card-visually-active",
            "event-card",
        ),
        width=f"{CARD_WIDTH_PX}px",
        height="120px",
        border_radius="16px",
        padding="12px",
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
        cursor="pointer",
        border=rx.cond(
            is_active,
            f"1.5px solid {MainState.theme_colors['aurora_teal']}",
            f"1px solid {MainState.theme_colors['aurora_teal']}22",
        ),
        background=rx.cond(
            MainState.dark_mode,
            f"linear-gradient(135deg, #0f172a 0%, {MainState.theme_colors['card_bg']} 100%)",
            f"linear-gradient(135deg, {MainState.theme_colors['bg']} 0%, {MainState.theme_colors['card_bg']} 100%)",
        ),
        on_click=MainState.select_event(event.id),
    )
