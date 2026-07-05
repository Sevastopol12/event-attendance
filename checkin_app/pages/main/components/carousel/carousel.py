import reflex as rx

from checkin_app.pages.main.state import MainState, EventItem
from .subcomponents import event_card
from .utils import carousel_controller_script
from .styles import DESKTOP_VIEWPORT_WIDTH, MOBILE_VIEWPORT_WIDTH, CARD_WIDTH_PX


def event_carousel() -> rx.Component:
    """The event carousel component."""

    actual_carousel = rx.vstack(
        carousel_progress_stack(),
        rx.center(
            rx.box(
                # Scroll Area
                rx.box(
                    rx.hstack(
                        rx.foreach(MainState.events, event_card),
                        spacing="4",
                        align="center",
                        width="max-content",
                    ),
                    class_name="carousel-scroll-viewport",
                    padding_left=f"calc(50% - {CARD_WIDTH_PX / 2}px)",
                    padding_right=f"calc(50% - {CARD_WIDTH_PX / 2}px)",
                    width="100%",
                    height="180px",
                    overflow_x="auto",
                    overflow_y="hidden",
                ),
                class_name="carousel-outer-boundary",
                width=rx.breakpoints(
                    sm=MOBILE_VIEWPORT_WIDTH, md=DESKTOP_VIEWPORT_WIDTH
                ),
                height="180px",
            ),
            width="100%",
        ),
        carousel_animation(),
        carousel_controller_script(),
        width="100%",
        spacing="2",
    )

    carousel_style = rx.cond(
        MainState.carousel_ready,
        dict(
            opacity="1",
            animation="fade_in 0.6s ease-out forwards",
            width="100%",
        ),
        dict(
            opacity="0",
            position="absolute",
            pointer_events="none",
            z_index="-100",
            width="100%",
        ),
    )

    skeleton = rx.center(
        rx.text("Loading events...", color="gray"),
        height="180px",
        width="100%",
    )

    return rx.cond(
        MainState.is_data_loaded,
        rx.box(
            rx.cond(
                ~MainState.carousel_ready,
                skeleton,
            ),
            # Render arrows outside the animated container so they remain fixed to the viewport
            rx.cond(
                MainState.carousel_ready,
                progress_button_stack(),
                rx.fragment(),
            ),
            rx.box(
                actual_carousel,
                style=carousel_style,
            ),
            width="100%",
            position="relative",
        ),
        skeleton,
    )


def carousel_progress_stack() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Event ",
            MainState.current_event_index,
            " of ",
            MainState.total_events_count,
            color=MainState.theme_colors["text_secondary"],
            font_family="Outfit",
            font_size="0.85rem",
            font_weight="500",
        ),
        rx.progress(
            value=(MainState.current_event_index / MainState.total_events_count) * 100,
            width="200px",
            color_scheme="teal",
            height="3px",
            radius="full",
        ),
        align="center",
        justify="center",
        margin_bottom="1.5rem",
        width="100%",
    )


def progress_button_stack() -> rx.Component:
    # Theme-aware style variables for buttons
    button_bg_color = rx.cond(
        MainState.dark_mode,
        "rgba(15, 23, 42, 0.75)",  # Semi-transparent dark slate
        "rgba(255, 255, 255, 0.85)",  # Semi-transparent white
    )

    button_border_color = f"1px solid {MainState.theme_colors['aurora_teal']}44"

    button_icon_color = MainState.theme_colors["aurora_teal"]

    move_previous = rx.box(
        rx.icon_button(
            rx.icon("chevron-left", size=20),
            variant="ghost",
            cursor="pointer",
            on_click=MainState.go_prev_event,
            disabled=~MainState.has_prev_event,
            style={
                "color": button_icon_color,
                "width": {"sm": "20px", "md": "28px"},
                "height": {"sm": "72px", "md": "96px"},
                "background": button_bg_color,
                "border": button_border_color,
                "border-radius": "0 8px 8px 0",
                "backdrop-filter": "blur(4px)",
                "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.15)",
            },
        ),
        position="absolute",
        left=0,
        top="50%",
        transform="translateY(-50%)",
        z_index="999",
    )

    move_forward = rx.box(
        rx.icon_button(
            rx.icon("chevron-right", size=20),
            variant="ghost",
            cursor="pointer",
            on_click=MainState.go_next_event,
            disabled=~MainState.has_next_event,
            style={
                "color": button_icon_color,
                "width": {"sm": "20px", "md": "28px"},
                "height": {"sm": "72px", "md": "96px"},
                "background": button_bg_color,
                "border": button_border_color,
                "border-radius": "8px 0 0 8px",
                "backdrop-filter": "blur(4px)",
                "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.15)",
            },
        ),
        position="absolute",
        right=0,
        top="50%",
        transform="translateY(-50%)",
        z_index="999",
    )

    return (
        rx.fragment(
            move_previous,
            move_forward,
        ),
    )


def carousel_animation() -> rx.Component:
    # Animation
    state_bridge = rx.input(
        id="scroll-bridge-input",
        style={"display": "none"},
        on_change=MainState.select_event_from_scroll,
    )

    ready_bridge = rx.input(
        id="carousel-ready-bridge",
        style={"display": "none"},
        on_change=MainState.mark_carousel_ready,
    )

    return rx.fragment(state_bridge, ready_bridge)
