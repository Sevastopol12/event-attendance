import reflex as rx

from checkin_app.domain import Department
from checkin_app.pages.main.state import MainState, DepartmentState

from checkin_app.styles.theme import NORTHERN_LIGHTS_COLORS

from ..styles import get_tile_base_styles, get_tile_hover_styles


def department_tile(dept: Department) -> rx.Component:
    """Renders a compact, modern department tile optimized for all screens."""
    attendance_count = DepartmentState.attendance_for_selected_event[dept.id]
    is_active = attendance_count > 0
    is_expired = DepartmentState.selected_event_is_expired

    # Extract number from name (e.g., "Department 1" -> "1")
    dept_number = dept.name.split(" ")[1]

    background_color = {
        "teal_dark": NORTHERN_LIGHTS_COLORS["dark"]["aurora_teal"],
        "teal_light": NORTHERN_LIGHTS_COLORS["light"]["aurora_teal"],
    }

    active_color = rx.cond(
        MainState.dark_mode,
        background_color["teal_dark"],
        background_color["teal_light"],
    )

    return rx.box(
        rx.flex(
            # Hero Department Number
            hero_stack(dept_number, is_active, background_color),
            # Attendee Counter
            attendee_counter_stack(
                is_active,
                attendance_count,
                background_color,
                active_color,
            ),
            direction=rx.breakpoints(xs="row", md="column"),
            align="center",
            justify=rx.breakpoints(xs="between", md="center"),
            width="100%",
            padding="0em 1.5em",
            min_width="100px",
            spacing="1",
        ),
        **get_tile_base_styles(is_active, is_expired),
        _hover=get_tile_hover_styles(is_active, is_expired),
        _pressed={
            "transform": rx.cond(is_expired, "none", "scale(0.97)"),
            "box_shadow": "none",
        },
        on_click=DepartmentState.open_department_form(dept.id),
        animation=rx.cond(
            dept.id == DepartmentState.last_toggled_department_id,
            "tile_flash 0.8s ease-out",
            "none",
        ),
        width="100%",
    )


def attendee_counter_stack(
    is_active: bool,
    attendance_count: int,
    background_color: dict[str, str],
    active_color: str,
) -> rx.Component:
    return (
        rx.hstack(
            rx.icon("user", size=14),
            rx.text(
                attendance_count,
                font_family="Outfit",
                font_size=rx.breakpoints(xs="0.85rem", sm="0.95rem", md="1rem"),
                font_weight="800",
            ),
            padding=rx.breakpoints(xs="0.2rem 0.6rem", sm="0.3rem 0.8rem"),
            border_radius="full",
            bg=rx.cond(
                is_active,
                rx.cond(
                    MainState.dark_mode,
                    f"{background_color['teal_dark']}20",
                    f"{background_color['teal_light']}15",
                ),
                rx.cond(
                    MainState.dark_mode,
                    "rgba(30, 41, 59, 0.4)",
                    "rgba(241, 245, 249, 0.8)",
                ),
            ),
            border=rx.cond(
                is_active,
                rx.cond(
                    MainState.dark_mode,
                    f"1px solid {background_color['teal_dark']}44",
                    f"1px solid {background_color['teal_light']}33",
                ),
                "1px solid transparent",
            ),
            color=rx.cond(
                is_active,
                active_color,
                "rgba(148, 163, 184, 0.5)",
            ),
            align="center",
            spacing="2",
            transition="all 0.3s ease",
        ),
    )


def hero_stack(
    dept_number: str, is_active: bool, background_color: dict[str, str]
) -> rx.Component:
    return (
        rx.text(
            dept_number,
            font_family="Outfit",
            font_size=rx.breakpoints(xs="1.75rem", sm="2rem", md="2.25rem"),
            font_weight="900",
            background=rx.cond(
                is_active,
                rx.cond(
                    MainState.dark_mode,
                    f"linear-gradient(to bottom right, {background_color['teal_dark']}, #2DD4BF)",
                    f"linear-gradient(to bottom right, {background_color['teal_light']}, #0D9488)",
                ),
                "none",
            ),
            background_clip=rx.cond(is_active, "text", "border-box"),
            color=rx.cond(
                is_active,
                "transparent",
                "rgba(148, 163, 184, 0.45)",
            ),
            line_height="1",
            margin_y="0.1rem",
        ),
    )
