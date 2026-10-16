from beanie import PydanticObjectId
from fastapi import APIRouter, Body, HTTPException, status, Depends, Query
from database.connection import Database

from datetime import datetime

from models.events import Event, EventCreate, EventUpdate
from typing import List

from auth.authenticate import authenticate

event_database = Database(Event)

event_router = APIRouter(tags=["Events"])

events = []


@event_router.get("/")
async def get_events(
    since: datetime | None = None,
    until: datetime | None = None,
    limit: int | None = Query(default=None, ge=1, le=1000),
):
    filters = []

    if since is not None:
        filters.append(Event.timestamp >= since)

    if until is not None:
        filters.append(Event.timestamp < until)

    query = Event.find(*filters).sort("-timestamp")

    if limit is not None:
        query = query.limit(limit)

    return await query.to_list()


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied ID does not exist"
        )
    return event


@event_router.post("/new")
async def create_event(body: EventCreate, user: str = Depends(authenticate)) -> dict:
    event = Event(**body.model_dump(), creator=user)
    await event_database.save(event)
    return {"message": "Event created successfully"}


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    event_instance = await event_database.get(id)
    if not event_instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied ID does not exist"
        )
    if event_instance.creator != user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not allowed: You are not the event creator",
        )
    success = await event_database.delete(id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete event after authorization check",
        )
    return {"message": "Event deleted successfully"}
