import reflex as rx
from checkin_app.pages.main.state import MainState
from checkin_app.components.background import aurora_background
from checkin_app.pages.main.components import (
    event_carousel,
    department_grid,
    status_strip,
    department_count_form,
    event_status_card,
    description_card,
)
from checkin_app.styles.theme import GLOBAL_CSS


@rx.page(route="/")
def main_page() -> rx.Component:
    """The main page view for event attendance.

    This page displays the current event's attendance status and
    serves as the shell for the application's primary functionality.
    """
    return aurora_background(
        rx.fragment(
            rx.html(f"<style>{GLOBAL_CSS}</style>"),
            rx.container(
                rx.vstack(
                    status_strip(),
                    event_carousel(),
                    # Responsive side-by-side layout for status and description
                    rx.flex(
                        event_status_card(),
                        description_card(),
                        direction="column",
                        width="100%",
                        spacing="7",
                        align="center",
                        justify="center",
                        wrap="wrap",
                    ),
                    department_grid(),
                    department_count_form(),
                    spacing="8",
                    align="center",
                    justify="center",
                    padding_top="12vh",
                    paddingBottom="5vh",
                    width="100%",
                ),
                size="4",
                width="100%",
                on_mount=MainState.on_load,
            ),
        )
    )
