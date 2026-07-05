import reflex as rx
from checkin_app.pages.main.state import MainState
from .subcomponents import live_attendance_block, event_timeline
from checkin_app.styles import get_unified_card_styles


unified_card_style = {
    "max_width": "800px",
    "padding": rx.breakpoints(xs="1rem", md="2rem"),
    "border_radius": "24px",
    "variant": "ghost",
    **get_unified_card_styles(MainState.dark_mode, MainState.theme_colors),
}


def event_status_card() -> rx.Component:
    """A unified event status card combining live attendance stats and the event timeline.

    The card follows the aurora glassmorphism aesthetic, leveraging the high-visual
    attendance block and timeline components.
    """
    actual_card = rx.card(
        rx.vstack(
            live_attendance_block(),
            rx.hstack(
                event_timeline(),
                width="100%",
                paddingTop="1rem",
            ),
            spacing="6",
            align="center",
        ),
        width="100%",
        **unified_card_style,
    )

    return rx.cond(
        MainState.is_data_loaded,
        actual_card,
        event_status_card_skeleton(),
    )


def event_status_card_skeleton() -> rx.Component:
    """Skeleton for the event status card that mirrors the actual layout geometry."""
    return rx.box(
        rx.vstack(
            # Attendance Block Skeleton
            rx.flex(
                rx.flex(
                    rx.vstack(
                        rx.skeleton(width="100px", height="1rem"),
                        rx.skeleton(width="140px", height="3rem"),
                        align="start",
                        spacing="2",
                    ),
                    rx.skeleton(width="1px", height="40px"),
                    rx.vstack(
                        rx.skeleton(width="100px", height="1rem"),
                        rx.skeleton(width="100px", height="3rem"),
                        align="start",
                        spacing="2",
                    ),
                    direction="row",
                    align="center",
                    spacing="6",
                    flex_wrap="wrap",
                ),
                rx.skeleton(width="60px", height="1.5rem", border_radius="full"),
                direction={"base": "column", "sm": "row"},
                justify={"base": "start", "sm": "between"},
                align={"base": "start", "sm": "center"},
                width="100%",
                gap="4",
            ),
            # Timeline Skeleton
            rx.box(
                rx.vstack(
                    rx.foreach(
                        range(3),
                        lambda i: rx.skeleton(
                            width="100%", height="2rem", border_radius="8px"
                        ),
                    ),
                    width="100%",
                    spacing="3",
                ),
                width="100%",
                padding_top="1rem",
            ),
            spacing="6",
            align="center",
        ),
        width="100%",
        **unified_card_style,
    )
