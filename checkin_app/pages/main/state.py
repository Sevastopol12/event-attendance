import reflex as rx
import asyncio
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

import pydantic
from checkin_app.domain import Department
from checkin_app.styles.theme import NORTHERN_LIGHTS_COLORS


class EventItem(pydantic.BaseModel):
    id: Optional[str]
    title: str
    time: str
    status: str
    is_expired: bool
    description: str
    start_at: datetime
    end_at: datetime


class MainState(rx.State):
    """State management for the main event attendance page.

    This state holds mock data for events, departments, and attendance counts
    to drive the UI during the skeleton development phase.
    """

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

    selected_event_id: str = "event_1"

    departments: List[Department] = [
        Department(id=f"dept_{i}", name=f"Department {i}") for i in range(1, 46)
    ]

    attendance: Dict[str, Dict[str, int]] = {
        "event_1": {f"dept_{i}": 10 for i in range(1, 46)},
        "event_2": {f"dept_{i}": 5 for i in range(1, 46)},
        "event_3": {f"dept_{i}": 0 for i in range(1, 46)},
        "event_4": {f"dept_{i}": 0 for i in range(1, 46)},
        "event_5": {f"dept_{i}": 0 for i in range(1, 46)},
        "event_6": {f"dept_{i}": 0 for i in range(1, 46)},
    }

    is_data_loaded: bool = False
    carousel_ready: bool = False

    dark_mode: bool = True

    # Department Form State
    selected_department_id: Optional[str] = None
    department_count_input: str = ""

    # Interaction Tracking
    last_toggled_department_id: Optional[str] = None
    last_selected_event_id: Optional[str] = None
    carousel_direction: str = "right"

    @rx.var
    def theme_colors(self) -> Dict[str, str]:
        """Returns the active theme color palette."""
        return NORTHERN_LIGHTS_COLORS["dark" if self.dark_mode else "light"]

    def toggle_dark_mode(self) -> None:
        """Toggles the dark mode setting."""
        self.dark_mode = not self.dark_mode

    @rx.event(background=True)
    async def on_load(self) -> None:
        """Simulates initial data fetching delay and sets the initial selected event."""
        async with self:
            await asyncio.sleep(2.0)

        # Find the first "On-going" event to start with
        ongoing_event = next((e for e in self.events if e.status == "On-going"), None)
        if ongoing_event:
            self.selected_event_id = ongoing_event.id
        elif self.events:
            self.selected_event_id = self.events[0].id

        self.carousel_ready = False
        self.is_data_loaded = True

    @rx.event
    def mark_carousel_ready(self) -> None:
        """Sets the carousel_ready state to True when notified by frontend JS."""
        self.carousel_ready = True

    @rx.var
    def selected_event(self) -> Optional[EventItem]:
        """Returns the selected event."""
        for event in self.events:
            if event.id == self.selected_event_id:
                return event
        return None

    @rx.var
    def selected_event_title(self) -> str:
        """Returns the title of the selected event."""
        event = self.selected_event
        return event.title if event else "No Event Selected"

    @rx.var
    def selected_event_status(self) -> str:
        """Returns the status of the selected event."""
        event = self.selected_event
        return event.status if event else ""

    @rx.var
    def selected_event_description(self) -> str:
        """Returns the description of the selected event."""
        event = self.selected_event
        return event.description if event else ""

    @rx.var
    def selected_event_is_expired(self) -> bool:
        """Returns whether the selected event is expired."""
        event = self.selected_event
        return event.is_expired if event else False

    @rx.event
    def select_event(self, event_id: str) -> None:
        """Updates the currently selected event ID.

        Args:
            event_id (str): The ID of the event to select.
        """
        self.selected_event_id = event_id

    @rx.event
    def select_event_from_scroll(self, event_id: str) -> None:
        """Triggered by client-side JS when scrolling stops on a card.

        Args:
            event_id (str): The ID of the event to select.
        """
        if not event_id or event_id.startswith("empty_"):
            return
        self.selected_event_id = event_id

    @rx.event
    def go_prev_event(self) -> None:
        """Go to the previous event."""
        current_idx = -1
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                current_idx = i
                break
        if current_idx > 0:
            self.carousel_direction = "left"
            self.selected_event_id = self.events[current_idx - 1].id

    @rx.event(background=True)
    def go_next_event(self) -> None:
        """Go to the next event."""
        current_idx = -1
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                current_idx = i
                break
        if current_idx != -1 and current_idx < len(self.events) - 1:
            self.carousel_direction = "right"
            self.selected_event_id = self.events[current_idx + 1].id

    @rx.var
    def total_events_count(self) -> int:
        """Returns the total number of events."""
        return len(self.events)

    @rx.var
    def current_event_index(self) -> int:
        """Returns the 1-based index of the current event."""
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                return i + 1
        return 0

    @rx.var
    def has_prev_event(self) -> bool:
        """Returns true if there is a previous event."""
        return self.current_event_index > 1

    @rx.var
    def has_next_event(self) -> bool:
        """Returns true if there is a next event."""
        return (
            self.current_event_index > 0
            and self.current_event_index < self.total_events_count
        )

    @rx.var
    def carousel_events(self) -> list[EventItem]:
        """Returns a list of three events: [previous, selected, next].

        Returns:
            A list containing the previous event, the currently selected event, and the next event.
            A placeholder dictionary with unique empty ids is used if no event exists in that position.
        """

        def get_empty(eid: str) -> EventItem:
            return EventItem(
                id=eid,
                title="",
                time="",
                status="",
                description="",
                is_expired=False,
                start_at=datetime.now(),
                end_at=datetime.now(),
            )

        # Find index of current selected event
        current_idx: int = -1
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                current_idx = i
                break

        if current_idx == -1:
            return [get_empty("empty_1"), get_empty("empty_2"), get_empty("empty_3")]

        prev_event: EventItem = (
            self.events[current_idx - 1] if current_idx > 0 else get_empty("empty_prev")
        )
        curr_event: EventItem = self.events[current_idx]

        next_event: EventItem = (
            self.events[current_idx + 1]
            if current_idx < len(self.events) - 1
            else get_empty("empty_next")
        )

        return [prev_event, curr_event, next_event]

    @rx.var
    def selected_event_progress_percent(self) -> float:
        """Calculates the current progress percentage of the selected event."""
        event = self.selected_event
        if not event:
            return 0.0

        now = datetime.now()
        if now < event.start_at:
            return 0.0
        if now > event.end_at:
            return 100.0

        total_duration = (event.end_at - event.start_at).total_seconds()
        elapsed = (now - event.start_at).total_seconds()

        if total_duration <= 0:
            return 0.0

        return min(100.0, max(0.0, (elapsed / total_duration) * 100))

    @rx.var
    def selected_event_progress_text(self) -> str:
        """Returns the formatted progress percentage text."""
        return f"{int(self.selected_event_progress_percent)}%"

    @rx.var
    def selected_event_start_time_formatted(self) -> str:
        """Returns the formatted start time of the selected event (e.g., 08:00 AM)."""
        event = self.selected_event
        return event.start_at.strftime("%I:%M %p") if event else ""

    @rx.var
    def selected_event_end_time_formatted(self) -> str:
        """Returns the formatted end time of the selected event (e.g., 10:00 AM)."""
        event = self.selected_event
        return event.end_at.strftime("%I:%M %p") if event else ""

    @rx.var
    def selected_event_timeline_lock_state(self) -> str:
        """Returns the lock state of the event timeline.

        'locked_start': Event hasn't started yet.
        'locked_end': Event has expired.
        'active': Event is currently on-going.
        """
        event = self.selected_event
        if not event:
            return "locked_start"

        now = datetime.now()
        if now < event.start_at:
            return "locked_start"
        if now > event.end_at:
            return "locked_end"
        return "active"

    @rx.var
    def selected_department_name(self) -> str:
        """Returns the name of the currently selected department for the form.

        Returns:
            str: The department name or an empty string if no department is selected.
        """
        if not self.selected_department_id:
            return ""
        
        for dept in self.departments:
            if dept.id == self.selected_department_id:
                return dept.name
        return ""

    @rx.var
    def attendance_for_selected_event(self) -> Dict[str, int]:
        """Returns the attendance counts for the currently selected event.

        Returns:
            Dict[str, int]: A dictionary mapping department names to their
            attendance count for the selected event.
        """
        return self.attendance.get(self.selected_event_id, {})

    @rx.var
    def present_department_count(self) -> int:
        """Returns the count of departments with at least one person present."""
        attendance = self.attendance_for_selected_event
        return sum(1 for count in attendance.values() if count > 0)

    @rx.var
    def total_people_present(self) -> int:
        """Returns the total number of people present across all departments."""
        attendance = self.attendance_for_selected_event
        return sum(attendance.values())

    @rx.var
    def total_departments_count(self) -> int:
        """Returns the total number of departments."""
        return len(self.departments)

    def toggle_attendance(self, dept_id: str) -> None:
        """Toggles attendance count for a specific department in the selected event.

        If the event is expired, the update is rejected. Otherwise, it increments
        the count if it was 0, and decrements if it was > 0.

        Args:
            dept_id (str): The ID of the department to toggle.
        """
        # Check if expired using the computed var's logic
        if self.selected_event_is_expired:
            return

        # Update attendance in the dictionary
        current_attendance = self.attendance.get(self.selected_event_id, {})
        count = current_attendance.get(dept_id, 0)

        # Mock toggle logic: 0 -> 1, 1 -> 0 (or increment/decrement)
        new_count = 1 if count == 0 else 0

        # Create a new dictionary to trigger state update in Reflex
        updated_event_attendance = current_attendance.copy()
        updated_event_attendance[dept_id] = new_count

        updated_all_attendance = self.attendance.copy()
        updated_all_attendance[self.selected_event_id] = updated_event_attendance

        self.attendance = updated_all_attendance

    def open_department_form(self, dept_id: str) -> None:
        """Opens the attendance count form for a specific department.

        Args:
            dept_id (str): The ID of the department.
        """
        if self.selected_event_is_expired:
            return

        self.selected_department_id = dept_id
        # Initialize input with current attendance count
        current_count = self.attendance_for_selected_event.get(dept_id, 0)
        self.department_count_input = str(current_count)

    def close_department_form(self) -> None:
        """Closes the attendance count form."""
        self.selected_department_id = None
        self.department_count_input = ""

    def set_department_count(self, value: str) -> None:
        """Updates the value of the attendance count input field.

        Args:
            value (str): The new input value.
        """
        self.department_count_input = value

    def increment_department_count(self) -> None:
        """Increments the attendance count input value by 1."""
        try:
            current = (
                int(self.department_count_input) if self.department_count_input else 0
            )
            self.department_count_input = str(current + 1)
        except ValueError:
            self.department_count_input = "1"

    def decrement_department_count(self) -> None:
        """Decrements the attendance count input value by 1, ensuring it doesn't go below 0."""
        try:
            current = (
                int(self.department_count_input) if self.department_count_input else 0
            )
            self.department_count_input = str(max(0, current - 1))
        except ValueError:
            self.department_count_input = "0"

    def save_department_count(self) -> None:
        """Saves the entered attendance count for the selected department.

        Validates that the input is a non-negative integer. Treats empty input as 0.
        """
        if not self.selected_department_id:
            return

        try:
            # Treat empty as 0, and ensure it's a non-negative integer
            count_val = (
                int(self.department_count_input) if self.department_count_input else 0
            )
            if count_val < 0:
                count_val = 0
        except ValueError:
            # If invalid input, treat as 0
            count_val = 0

        # Update attendance in the dictionary
        current_attendance = self.attendance.get(self.selected_event_id, {})
        updated_event_attendance = current_attendance.copy()
        updated_event_attendance[self.selected_department_id] = count_val

        updated_all_attendance = self.attendance.copy()
        updated_all_attendance[self.selected_event_id] = updated_event_attendance

        self.attendance = updated_all_attendance

        # Mark as last toggled for visual feedback (pulse animation)
        self.last_toggled_department_id = self.selected_department_id

        # Close form after successful save
        self.close_department_form()
