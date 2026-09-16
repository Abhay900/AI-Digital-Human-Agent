from pydantic import BaseModel


class MovementProfile(BaseModel):
    gesture_style: str = "natural"
    hand_movement_style: str = "natural"
    body_movement_style: str = "natural"
    movement_speed: str = "natural"


class PersonProfile(BaseModel):
    person_id: str
    display_name: str
    movement: MovementProfile
    voice_profile: str | None = None
    face_profile: str | None = None
    expression_style: str = "natural"