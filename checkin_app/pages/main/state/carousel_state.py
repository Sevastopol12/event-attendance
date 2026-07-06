import reflex as rx
from typing import List, Optional
from datetime import datetime
from checkin_app.domain import EventItem
from .department_state import DepartmentState


class CarouselState(rx.State):
    """Substate handling carousel navigation and display."""

    events: List[EventItem] = []
    selected_event_id: str = ""
    carousel_ready: bool = False
    carousel_direction: str = "right"
    last_selected_event_id: Optional[str] = None

    @rx.var
    def selected_event(self) -> Optional[EventItem]:
        for event in self.events:
            if event.id == self.selected_event_id:
                return event
        return None

    @rx.var
    def selected_event_title(self) -> str:
        event = self.selected_event
        return event.title if event else "No Event Selected"

    @rx.var
    def selected_event_status(self) -> str:
        event = self.selected_event
        return event.status if event else ""

    @rx.var
    def selected_event_description(self) -> str:
        event = self.selected_event
        return event.description if event else ""

    @rx.var
    def selected_event_is_expired(self) -> bool:
        event = self.selected_event
        return event.is_expired if event else False

    @rx.var
    def selected_event_progress_percent(self) -> float:
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
        return f"{int(self.selected_event_progress_percent)}%"

    @rx.var
    def selected_event_start_time_formatted(self) -> str:
        event = self.selected_event
        return event.start_at.strftime("%I:%M %p") if event else ""

    @rx.var
    def selected_event_end_time_formatted(self) -> str:
        event = self.selected_event
        return event.end_at.strftime("%I:%M %p") if event else ""

    @rx.var
    def selected_event_timeline_lock_state(self) -> str:
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
    def total_events_count(self) -> int:
        return len(self.events)

    @rx.var
    def current_event_index(self) -> int:
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                return i + 1
        return 0

    @rx.var
    def has_prev_event(self) -> bool:
        return self.current_event_index > 1

    @rx.var
    def has_next_event(self) -> bool:
        return (
            self.current_event_index > 0
            and self.current_event_index < self.total_events_count
        )

    @rx.var
    def carousel_events(self) -> List[EventItem]:
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

        current_idx = -1
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                current_idx = i
                break

        if current_idx == -1:
            return [get_empty("empty_1"), get_empty("empty_2"), get_empty("empty_3")]

        prev_event = (
            self.events[current_idx - 1] if current_idx > 0 else get_empty("empty_prev")
        )
        curr_event = self.events[current_idx]

        next_event = (
            self.events[current_idx + 1]
            if current_idx < len(self.events) - 1
            else get_empty("empty_next")
        )

        return [prev_event, curr_event, next_event]

    @rx.event
    def mark_carousel_ready(self) -> None:
        self.carousel_ready = True

    async def _sync_department_state(self) -> None:
        """Push current event selection to DepartmentState."""
        ds = await self.get_state(DepartmentState)
        ds.selected_event_id = self.selected_event_id
        ds.selected_event_is_expired = self.selected_event_is_expired

    @rx.event
    async def select_event(self, event_id: str) -> None:
        self.selected_event_id = event_id
        await self._sync_department_state()

    @rx.event
    async def select_event_from_scroll(self, event_id: str) -> None:
        if not event_id or event_id.startswith("empty_"):
            return
        self.selected_event_id = event_id
        await self._sync_department_state()

    @rx.event
    async def go_prev_event(self) -> None:
        current_idx = -1
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                current_idx = i
                break
        if current_idx > 0:
            self.carousel_direction = "left"
            self.selected_event_id = self.events[current_idx - 1].id
            await self._sync_department_state()

    @rx.event
    async def go_next_event(self) -> None:
        current_idx = -1
        for i, event in enumerate(self.events):
            if event.id == self.selected_event_id:
                current_idx = i
                break
        if current_idx != -1 and current_idx < len(self.events) - 1:
            self.carousel_direction = "right"
            self.selected_event_id = self.events[current_idx + 1].id
            await self._sync_department_state()
