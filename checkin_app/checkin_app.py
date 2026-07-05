"""
Main entry point for the Reflex application.
"""

import reflex as rx
from rxconfig import config
from .pages import main_page

app = rx.App(
    stylesheets=[
        "/styles.css",
    ],
)
