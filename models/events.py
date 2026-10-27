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

    creator: str

    humidity: float
    temperature: float
    relative_pressure: float
    abs_pressure: float
    ppm: float
    rain_reading: int
    # Sensor model information - for future treaceability
    humidity_sensor: str
    temperature_sensor: str
    relative_pressure_sensor: str
    abs_pressure_sensor: str
    ppm_sensor: str
    rain_reading_sensor: str

    class Config:
        json_schema_extra = {
            "example": {
                "humidity": 14.5,
                "temperature": 27.3,
                "relative_pressure": 1.0,
                "abs_pressure": 1.0,
                "ppm": 3.0,
                "rain_reading": 1,
                "humidity_sensor": "dht11",
                "temperature_sensor": "dht11",
                "relative_pressure_sensor": "bmp180",
                "abs_pressure_sensor": "bmp180",
                "ppm_sensor": "mq-135",
                "rain_reading_sensor": "mh-rd yl-83",
            }
        }

    class Settings:
        name = "events"
        indexes = ["timestamp"]


class EventCreate(BaseModel):
    humidity: float
    temperature: float
    relative_pressure: float
    abs_pressure: float
    ppm: float
    rain_reading: int
    humidity_sensor: str
    temperature_sensor: str
    relative_pressure_sensor: str
    abs_pressure_sensor: str
    ppm_sensor: str
    rain_reading_sensor: str

    model_config = ConfigDict(extra="forbid")


class EventUpdate(BaseModel):
    humidity: float | None = None
    temperature: float | None = None
    relative_pressure: float | None = None
    abs_pressure: float | None = None
    ppm: float | None = None
    rain_reading: int | None = None
    humidity_sensor: str | None = None
    temperature_sensor: str | None = None
    relative_pressure_sensor: str | None = None
    abs_pressure_sensor: str | None = None
    ppm_sensor: str | None = None
    rain_reading_sensor: str | None = None

    model_config = ConfigDict(extra="forbid")
