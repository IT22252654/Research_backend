from fastapi import APIRouter
from app.schemas.mood_schema import MoodCheckin, MoodData
from app.services.mood_service import save_mood

router = APIRouter(prefix="/mood", tags=["Mood"])

@router.post("/checkin")
def mood_checkin(data: MoodCheckin):
    result = save_mood(data.child_id, data.mood, data.note)
    return {"status": "success", "data": {
        "id": result.id,
        "child_id": result.child_id,
        "mood": result.mood,
        "note": result.note
    }}

@router.post("/store")
def store_mood(data: MoodData):
    result = save_mood(data.userId, data.mood, data.datetime)
    return {"status": "success", "data": result}
