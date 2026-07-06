from datetime import datetime
from typing import Optional
import pydantic

class Department(pydantic.BaseModel):
    """Represents a department within the organization.
    
    Attributes:
        id (str): Unique identifier for the department (e.g., 'dept_1').
        name (str): Display name of the department (e.g., 'Department 1').
    """
    id: str
    name: str

class AttendanceRecord(pydantic.BaseModel):
    """Represents an attendance count for a specific event and department.
    
    Attributes:
        event_id (str): Unique identifier of the event.
        department_id (str): Unique identifier of the department.
        count (int): Number of people present.
    """
    event_id: str
    department_id: str
    count: int


class EventItem(pydantic.BaseModel):
    id: Optional[str]
    title: str
    time: str
    status: str
    is_expired: bool
    description: str
    start_at: datetime
    end_at: datetime

