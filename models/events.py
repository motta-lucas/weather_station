from beanie import Document
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from uuid import UUID, uuid4
from typing import List, Optional
import os


class Event(Document):
    id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=lambda: datetime.now().astimezone())
    device_id: str = "weather_station_01"

    humidity: float
    temperature: float
    relative_pressure: float
    abs_pressure: float
    ppm: float
    rain_reading: int

    class Config:
        json_schema_extra = {
            "example": {
                "humidity": 14.5,
                "temperature": 27.3,
                "relative_pressure": 1.0,
                "abs_pressure": 1.0,
                "ppm": 3.0,
                "rain_reading": 1,
            }
        }

    class Settings:
        name = "events"


class EventUpdate(Document):
    humidity: float | None = None
    temperature: float | None = None
    relative_pressure: float | None = None
    abs_pressure: float | None = None
    ppm: float | None = None
    rain_reading: int | None = None

    model_config = ConfigDict(extra="forbid")
