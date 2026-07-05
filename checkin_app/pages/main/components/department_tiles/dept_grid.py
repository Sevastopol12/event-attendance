import reflex as rx

from checkin_app.pages.main.state import MainState
from .subcomponents import department_tile
from .styles import unified_grid_style


def department_grid_skeleton() -> rx.Component:
    """Skeleton loading layout matching the updated compact grid geometry."""
    return rx.grid(
        rx.foreach(
            range(18),
            lambda i: rx.skeleton(
                width="100%",
                height=rx.breakpoints(xs="70px", sm="100px", md="110px"),
                border_radius="12px",
            ),
        ),
        **unified_grid_style,
    )


def department_grid() -> rx.Component:
    """Renders a responsive, space-efficient grid of department tiles."""
    actual_grid = rx.grid(
        rx.foreach(MainState.departments, department_tile), 
        **unified_grid_style
    )

    return rx.cond(
        MainState.is_data_loaded,
        actual_grid,
        department_grid_skeleton(),
    )
