import reflex as rx
from typing import List, Dict, Optional
from checkin_app.domain import Department


class DepartmentState(rx.State):
    """Substate handling department grid, attendance, and form."""

    departments: List[Department] = []
    attendance: Dict[str, Dict[str, int]] = {}

    selected_event_id: str = ""
    selected_event_is_expired: bool = False

    selected_department_id: Optional[str] = None
    department_count_input: str = ""
    last_toggled_department_id: Optional[str] = None

    @rx.var
    def selected_department_name(self) -> str:
        if not self.selected_department_id:
            return ""

        for dept in self.departments:
            if dept.id == self.selected_department_id:
                return dept.name
        return ""

    @rx.var
    def attendance_for_selected_event(self) -> Dict[str, int]:
        return self.attendance.get(self.selected_event_id, {})

    @rx.var
    def present_department_count(self) -> int:
        attendance = self.attendance_for_selected_event
        return sum(1 for count in attendance.values() if count > 0)

    @rx.var
    def total_people_present(self) -> int:
        attendance = self.attendance_for_selected_event
        return sum(attendance.values())

    @rx.var
    def total_departments_count(self) -> int:
        return len(self.departments)

    @rx.event(background=True)
    async def toggle_attendance(self, dept_id: str) -> None:
        async with self:
            if self.selected_event_is_expired:
                return

            current_attendance = self.attendance.get(self.selected_event_id, {})
            count = current_attendance.get(dept_id, 0)
            new_count = 1 if count == 0 else 0

            updated_event_attendance = current_attendance.copy()
            updated_event_attendance[dept_id] = new_count

            updated_all_attendance = self.attendance.copy()
            updated_all_attendance[self.selected_event_id] = updated_event_attendance

            self.attendance = updated_all_attendance

    @rx.event
    def open_department_form(self, dept_id: str) -> None:
        if self.selected_event_is_expired:
            return

        self.selected_department_id = dept_id
        current_count = self.attendance_for_selected_event.get(dept_id, 0)
        self.department_count_input = str(current_count)

    @rx.event
    def close_department_form(self) -> None:
        self.selected_department_id = None
        self.department_count_input = ""

    @rx.event
    def set_department_count(self, value: str) -> None:
        self.department_count_input = value

    @rx.event
    def increment_department_count(self) -> None:
        try:
            current = int(self.department_count_input) if self.department_count_input else 0
            self.department_count_input = str(current + 1)
        except ValueError:
            self.department_count_input = "1"

    @rx.event
    def decrement_department_count(self) -> None:
        try:
            current = int(self.department_count_input) if self.department_count_input else 0
            self.department_count_input = str(max(0, current - 1))
        except ValueError:
            self.department_count_input = "0"

    @rx.event(background=True)
    async def save_department_count(self) -> None:
        async with self:
            if not self.selected_department_id:
                return

            try:
                count_val = int(self.department_count_input) if self.department_count_input else 0
                if count_val < 0:
                    count_val = 0
            except ValueError:
                count_val = 0

            current_attendance = self.attendance.get(self.selected_event_id, {})
            updated_event_attendance = current_attendance.copy()
            updated_event_attendance[self.selected_department_id] = count_val

            updated_all_attendance = self.attendance.copy()
            updated_all_attendance[self.selected_event_id] = updated_event_attendance

            self.attendance = updated_all_attendance
            self.last_toggled_department_id = self.selected_department_id
            self.close_department_form()
