import reflex as rx
from checkin_app.pages.main.state import MainState


def live_attendance_block() -> rx.Component:
    """A professionally redesigned dashboard block rendering live attendance stats.

    Returns only the inner content to be wrapped in a parent card.
    """
    return rx.flex(
        # Group 1: Stats and Divider
        rx.flex(
            # Stat 1: Departments
            department_count_stack(),
            # Vertical Divider
            rx.box(
                width="1px",
                height="40px",
                background_color=rx.cond(
                    MainState.dark_mode,
                    "rgba(255, 255, 255, 0.15)",
                    "rgba(0, 0, 0, 0.15)",
                ),
                align_self="center",
                flex_shrink="0",
                display=rx.breakpoints(xs="none", sm="block"),
            ),
            # Stat 2: Total People
            department_people_count_stack(),
            direction="row",
            align="center",
            spacing="6",
            flex_wrap="wrap",
        ),
        # Group 2: Live Indicator
        rx.cond(
            MainState.selected_event_status == "On-going",
            live_indicator_stack(),
            rx.fragment(),
        ),
        direction=rx.breakpoints(xs="column", sm="row"),
        justify=rx.breakpoints(xs="start", sm="between"),
        align=rx.breakpoints(xs="start", sm="center"),
        width="100%",
        gap="4",
    )


def department_count_stack() -> rx.Component:
    return (
        rx.vstack(
            # Department count
            rx.flex(
                rx.icon(
                    "building-2",
                    size=16,
                    color=MainState.theme_colors["text_secondary"],
                ),
                rx.text(
                    "DEPARTMENTS",
                    font_family="Outfit",
                    font_size="0.7rem",
                    font_weight="700",
                    text_transform="uppercase",
                    letter_spacing="0.1em",
                    color=MainState.theme_colors["text_secondary"],
                    white_space="nowrap",
                ),
                align="center",
                spacing="2",
            ),
            # People count
            rx.hstack(
                rx.text(
                    MainState.present_department_count,
                    font_family="Outfit",
                    font_size=rx.breakpoints(xs="2.2rem", sm="3rem", md="3.5rem"),
                    font_weight="800",
                    color=MainState.theme_colors["text_primary"],
                    text_shadow=f"0 0 20px {MainState.theme_colors['aurora_teal']}44",
                ),
                rx.text(
                    " / ",
                    MainState.total_departments_count,
                    font_family="Outfit",
                    font_size="1.1rem",
                    font_weight="400",
                    color=MainState.theme_colors["text_secondary"],
                ),
                align="center",
                spacing="1",
            ),
            align="start",
            spacing="1",
            flex_shrink="0",
        ),
    )


def department_people_count_stack() -> rx.Component:
    return (
        rx.vstack(
            rx.flex(
                rx.icon(
                    "users", size=16, color=MainState.theme_colors["text_secondary"]
                ),
                rx.text(
                    "TOTAL PEOPLE",
                    font_family="Outfit",
                    font_size="0.7rem",
                    font_weight="700",
                    text_transform="uppercase",
                    letter_spacing="0.1em",
                    color=MainState.theme_colors["text_secondary"],
                    white_space="nowrap",
                ),
                align="center",
                spacing="2",
            ),
            rx.text(
                MainState.total_people_present,
                font_family="Outfit",
                font_size=rx.breakpoints(xs="2.2rem", sm="3rem", md="3.5rem"),
                font_weight="800",
                color=MainState.theme_colors["text_primary"],
                text_shadow=f"0 0 20px {MainState.theme_colors['aurora_teal']}44",
            ),
            align="start",
            spacing="1",
            flex_shrink="0",
        ),
    )


def live_indicator_stack() -> rx.Component:
    return (
        rx.hstack(
            rx.box(
                width="6px",
                height="6px",
                border_radius="20px",
                background_color=MainState.theme_colors["aurora_teal"],
                animation="pulse 1.5s infinite",
                marginRight="6px",
                box_shadow=f"0 0 8px {MainState.theme_colors['aurora_teal']}",
            ),
            rx.text(
                "LIVE",
                font_family="Outfit",
                font_weight="800",
                font_size="0.7rem",
                color=MainState.theme_colors["aurora_teal"],
                letter_spacing="0.05em",
            ),
            align="center",
            background_color=rx.cond(
                MainState.dark_mode,
                "rgba(45, 212, 191, 0.15)",
                "rgba(13, 148, 136, 0.15)",
            ),
            border=f"1px solid {MainState.theme_colors['aurora_teal']}",
            box_shadow="0 0 10px rgba(45, 212, 191, 0.2)",
            variant="ghost",
            padding="2px 8px",
            flex_shrink="0",
        ),
    )
