# src/domain/models.py
from __future__ import annotations
from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Dict

from sqlalchemy import Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSONB, UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all database models."""

    pass


class Event(Base):
    """
    Represents a check-in event.

    Attributes:
        event_id (UUID): Unique identifier for the event.
        title (str): Title of the event.
        start_time (datetime): Start timestamp of the event.
        end_time (datetime): End timestamp of the event.
    """

    __tablename__ = "events"
    __table_args__ = {"schema": "Events"}

    event_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    title: Mapped[str] = mapped_column(Text, nullable=False)
    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    def __repr__(self) -> str:
        return f"Event(event_id={self.event_id}, title={self.title})"


class Attendance(Base):
    """
    Represents attendance records for an event.

    Attributes:
        record_id (UUID): Unique identifier for the record.
        event_id (UUID): Foreign key referencing the event.
        attendees (Dict[str, Any]): JSONB dictionary of attendees.
    """

    __tablename__ = "attendance"
    __table_args__ = {"schema": "Events"}

    record_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    event_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("Events.events.event_id"), nullable=False
    )
    attendees: Mapped[Dict[str, Any]] = mapped_column(JSONB, default=dict)

    def __repr__(self) -> str:
        return f"Attendance(record_id={self.record_id}, event_id={self.event_id})"
