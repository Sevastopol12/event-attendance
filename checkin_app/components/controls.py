import reflex as rx

from checkin_app.pages.main.state import MainState


def custom_checkbox(
    value: rx.Var,
    on_change: rx.EventHandler,
    is_disabled: rx.Var = False,
) -> rx.Component:
    """A custom-styled checkbox component adhering to Northern Lights theme."""
    return rx.box(
        rx.box(
            rx.icon(
                "check",
                color=MainState.theme_colors["text_primary"],
                size=12,
                display=rx.cond(value, "block", "none"),
            ),
            width="18px",
            height="18px",
            border_radius="4px",
            background=rx.cond(
                value,
                MainState.theme_colors["aurora_teal"],
                "transparent",
            ),
            border=rx.cond(
                value,
                rx.cond(
                    MainState.dark_mode,
                    "1px solid #2DD4BF",
                    "1px solid #0D9488",
                ),
                rx.cond(
                    MainState.dark_mode,
                    "1px solid #94A3B8",
                    "1px solid #475569",
                ),
            ),
            display="flex",
            align="center",
            justify="center",
            transition="all 0.2s ease",
            cursor=rx.cond(is_disabled, "not-allowed", "pointer"),
            _hover={
                "border": rx.cond(
                    is_disabled,
                    rx.cond(
                        MainState.dark_mode,
                        "1px solid #94A3B8",
                        "1px solid #475569",
                    ),
                    rx.cond(
                        MainState.dark_mode,
                        "1px solid #22D3EE",
                        "1px solid #0891B2",
                    ),
                ),
            },
        ),
        on_click=on_change,
        pointer_events=rx.cond(is_disabled, "none", "auto"),
        display="flex",
        align="center",
        justify="center",
        opacity=rx.cond(is_disabled, "0.5", "1"),
    )
