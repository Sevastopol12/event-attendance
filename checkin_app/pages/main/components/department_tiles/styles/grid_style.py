import reflex as rx

unified_grid_style = {
    "grid_template_columns": rx.breakpoints(
        xs="1fr",
        sm="repeat(3, 1fr)",
        md="repeat(4, 1fr)",
        lg="repeat(5, 1fr)",
        xl="repeat(5, 1fr)",
    ),
    "gap": rx.breakpoints(xs="1rem", sm="1rem", md="1.25rem"),
    "width": "100%",
    "padding_x": rx.breakpoints(xs="1rem", sm="1.5rem", md="2rem"),
    "justify_content": "center",
}
