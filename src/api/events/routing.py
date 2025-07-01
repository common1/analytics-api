from fastapi import APIRouter
from .schemas import (
    EventSchema,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema
)

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    # a bunch of items in a table
    return {
        "results": [
            {"id": 1}, {"id": 2}, {"id": 3}
        ],
        "count": 3
    }

@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    # a bunch of items in a table
    print(payload.page)
    return {"id": 123}

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single row
    return {"id": event_id}

@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    # a single row
    print(payload.description)
    return {"id": event_id}

# @router.delete("/{event_id}")
# def delete_event(event_id: int) -> EventSchema:
#     # a single row
#     return {"id": event_id}
