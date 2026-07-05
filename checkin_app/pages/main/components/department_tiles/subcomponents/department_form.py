import reflex as rx
from checkin_app.pages.main.state import MainState
from checkin_app.styles.theme import NORTHERN_LIGHTS_COLORS


def department_count_form() -> rx.Component:
    """A compact, themed form for updating the attendance count of a department."""

    # Dynamic styles based on theme
    glass_bg = rx.cond(
        MainState.dark_mode,
        "rgba(2, 6, 23, 0.85)",
        "rgba(255, 255, 255, 0.85)",
    )

    glass_border = rx.cond(
        MainState.dark_mode,
        f"1px solid rgba(148, 163, 184, 0.2)",
        f"1px solid rgba(71, 85, 105, 0.2)",
    )

    # Aurora accent colors
    accent_color = rx.cond(
        MainState.dark_mode,
        NORTHERN_LIGHTS_COLORS["dark"]["aurora_teal"],
        NORTHERN_LIGHTS_COLORS["light"]["aurora_teal"],
    )

    return rx.cond(
        MainState.selected_department_id,
        rx.box(
            # Backdrop for the modal
            rx.center(
                rx.vstack(
                    # Form Header
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                "Update Attendance",
                                font_family="Outfit",
                                font_weight="700",
                                size="4",
                                color=MainState.theme_colors["text_primary"],
                            ),
                            rx.text(
                                rx.cond(
                                    MainState.selected_department_id,
                                    MainState.selected_department_name,
                                    "",
                                ),
                                font_family="Outfit",
                                font_size="0.9rem",
                                color=MainState.theme_colors["text_secondary"],
                            ),
                            align="start",
                            spacing="0",
                        ),
                        rx.icon(
                            tag="x",
                            size=20,
                            cursor="pointer",
                            on_click=MainState.close_department_form,
                            color=MainState.theme_colors["text_secondary"],
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        margin_bottom="1.5rem",
                    ),
                    # Stepper Input Field
                    rx.vstack(
                        rx.text(
                            "Number of people present",
                            font_family="Outfit",
                            font_size="0.8rem",
                            font_weight="500",
                            color=MainState.theme_colors["text_secondary"],
                            text_align="left",
                            width="100%",
                        ),
                        rx.hstack(
                            # Decrement Button
                            rx.button(
                                rx.icon(tag="minus", size=18),
                                on_click=MainState.decrement_department_count,
                                width="40px",
                                height="56px",
                                padding="0",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                border_radius="8px",
                                cursor="pointer",
                                bg=rx.cond(
                                    MainState.dark_mode,
                                    "rgba(15, 23, 42, 0.5)",
                                    "rgba(241, 245, 249, 0.8)",
                                ),
                                border=glass_border,
                                color=MainState.theme_colors["text_primary"],
                                _hover={
                                    "bg": rx.cond(
                                        MainState.dark_mode,
                                        "rgba(30, 41, 59, 0.7)",
                                        "rgba(226, 232, 240, 0.9)",
                                    ),
                                    "transform": "scale(0.95)",
                                },
                            ),
                            # Numeric Input
                            rx.input(
                                value=MainState.department_count_input,
                                on_change=MainState.set_department_count,
                                placeholder="0",
                                type="number",
                                font_family="Outfit",
                                flex="1",
                                height="56px",
                                margin="0",
                                text_align="center",
                                border_radius="8px",
                                bg=rx.cond(
                                    MainState.dark_mode,
                                    "rgba(15, 23, 42, 0.5)",
                                    "rgba(241, 245, 249, 0.8)",
                                ),
                                border=glass_border,
                                color=MainState.theme_colors["text_primary"],
                                _focus={
                                    "border": f"1px solid {accent_color}",
                                    "box_shadow": f"0 0 0 2px {accent_color}33",
                                },
                            ),
                            # Increment Button
                            rx.button(
                                rx.icon(tag="plus", size=18),
                                on_click=MainState.increment_department_count,
                                width="40px",
                                height="56px",
                                padding="0",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                border_radius="8px",
                                cursor="pointer",
                                bg=rx.cond(
                                    MainState.dark_mode,
                                    "rgba(15, 23, 42, 0.5)",
                                    "rgba(241, 245, 249, 0.8)",
                                ),
                                border=glass_border,
                                color=MainState.theme_colors["text_primary"],
                                _hover={
                                    "bg": rx.cond(
                                        MainState.dark_mode,
                                        "rgba(30, 41, 59, 0.7)",
                                        "rgba(226, 232, 240, 0.9)",
                                    ),
                                    "transform": "scale(0.95)",
                                },
                            ),
                            align="center",
                            spacing="3",
                            width="100%",
                            display="flex",
                            align_items="center",
                        ),
                        align="start",
                        spacing="3",
                        width="100%",
                    ),
                    # Action Buttons
                    rx.hstack(
                        rx.button(
                            "Cancel",
                            on_click=MainState.close_department_form,
                            variant="outline",
                            font_family="Outfit",
                            font_size="0.9rem",
                            color=MainState.theme_colors["text_secondary"],
                            width="100px",
                            height="48px",
                            border_radius="8px",
                            cursor="pointer",
                        ),
                        rx.button(
                            "Save Changes",
                            on_click=MainState.save_department_count,
                            bg=accent_color,
                            color="white",
                            font_family="Outfit",
                            font_weight="600",
                            font_size="0.9rem",
                            width="140px",
                            height="48px",
                            border_radius="8px",
                            cursor="pointer",
                            _hover={
                                "opacity": "0.9",
                                "transform": "scale(0.98)",
                            },
                        ),
                        justify="end",
                        width="100%",
                        margin_top="2rem",
                        spacing="3",
                    ),
                    align="center",
                    spacing="4",
                    padding="2rem",
                    width=rx.breakpoints(sm="90%", md="380px"),
                    background=glass_bg,
                    backdrop_filter="blur(16px)",
                    border=glass_border,
                    border_radius="24px",
                    box_shadow=rx.cond(
                        MainState.dark_mode,
                        "0 20px 40px rgba(0,0,0,0.4)",
                        "0 20px 40px rgba(0,0,0,0.1)",
                    ),
                    animation="soft_pop 0.3s ease-out",
                ),
                position="fixed",
                top="0",
                left="0",
                width="100vw",
                height="100vh",
                background="rgba(0,0,0,0.5)",
                z_index="1000",
            ),
            rx.fragment(),
        ),
    )
