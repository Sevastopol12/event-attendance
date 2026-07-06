import reflex as rx
from typing import Dict
from datetime import datetime, timedelta

from checkin_app.domain import Department, EventItem
from checkin_app.styles.theme import NORTHERN_LIGHTS_COLORS
from .carousel_state import CarouselState
from .department_state import DepartmentState


class MainState(rx.State):
    """Global theme + page lifecycle orchestrator. Owns no event/department data."""

    is_data_loaded: bool = False
    dark_mode: bool = True

    @rx.var
    def theme_colors(self) -> Dict[str, str]:
        """Returns the active theme color palette."""
        return NORTHERN_LIGHTS_COLORS["dark" if self.dark_mode else "light"]

    def toggle_dark_mode(self) -> None:
        """Toggles the dark mode setting."""
        self.dark_mode = not self.dark_mode

    @rx.event(background=True)
    async def on_load(self) -> None:
        """Orchestrates initial data load and pushes to independent states."""
        events: list[EventItem] = [
            EventItem(
                id="event_1",
                title="Morning General Assembly",
                time="08:00 AM",
                status="Expired",
                is_expired=True,
                description="Opening ceremony and general briefing for all participants. Key updates on the event schedule and objectives.",
                start_at=datetime.now() - timedelta(hours=4),
                end_at=datetime.now() - timedelta(hours=2),
            ),
            EventItem(
                id="event_2",
                title="Technical Workshop",
                time="10:30 AM",
                status="On-going",
                is_expired=False,
                description="Hands-on technical session focusing on advanced implementation strategies and best practices in the field.",
                start_at=datetime.now() - timedelta(hours=1),
                end_at=datetime.now() + timedelta(hours=1),
            ),
            EventItem(
                id="event_3",
                title="Lunch Networking",
                time="12:00 PM",
                status="Not yet started",
                is_expired=False,
                description="Informal networking lunch to connect with peers and industry experts from various departments.",
                start_at=datetime.now() + timedelta(hours=1),
                end_at=datetime.now() + timedelta(hours=2),
            ),
            EventItem(
                id="event_4",
                title="Advanced AI Seminar",
                time="02:00 PM",
                status="Not yet started",
                is_expired=False,
                description="Deep dive into large language models and their practical applications in software engineering.",
                start_at=datetime.now() + timedelta(hours=3),
                end_at=datetime.now() + timedelta(hours=4),
            ),
            EventItem(
                id="event_5",
                title="Industry Panel Discussion",
                time="04:00 PM",
                status="Not yet started",
                is_expired=False,
                description="Experts from top tech companies discuss the future of full-stack development.",
                start_at=datetime.now() + timedelta(hours=5),
                end_at=datetime.now() + timedelta(hours=6),
            ),
            EventItem(
                id="event_6",
                title="Closing Keynote",
                time="06:00 PM",
                status="Not yet started",
                is_expired=False,
                description="Final wrap-up of the day's events and closing remarks from the organizers.",
                start_at=datetime.now() + timedelta(hours=7),
                end_at=datetime.now() + timedelta(hours=8),
            ),
        ]

        departments = [
            Department(id=f"dept_{i}", name=f"Department {i}") for i in range(1, 46)
        ]

        attendance = {
            "event_1": {f"dept_{i}": 10 for i in range(1, 46)},
            "event_2": {f"dept_{i}": 5 for i in range(1, 46)},
            "event_3": {f"dept_{i}": 0 for i in range(1, 46)},
            "event_4": {f"dept_{i}": 0 for i in range(1, 46)},
            "event_5": {f"dept_{i}": 0 for i in range(1, 46)},
            "event_6": {f"dept_{i}": 0 for i in range(1, 46)},
        }

        # Find ongoing event
        ongoing = next((e for e in events if e.status == "On-going"), events[0])

        async with self:
            # Push to CarouselState
            carousel_state = await self.get_state(CarouselState)
            carousel_state.events = events
            carousel_state.selected_event_id = ongoing.id

            # Push to DepartmentState
            department_state = await self.get_state(DepartmentState)
            department_state.departments = departments
            department_state.attendance = attendance
            department_state.selected_event_id = ongoing.id
            department_state.selected_event_is_expired = ongoing.is_expired

            self.is_data_loaded = True
