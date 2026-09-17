from pydantic import BaseModel, Field


class MovementProfile(BaseModel):
    """Person-specific movement and gesture characteristics."""

    gesture_style: str = "natural"
    hand_movement_style: str = "natural"
    body_movement_style: str = "natural"
    movement_speed: str = "natural"

    gesture_frequency: str = "moderate"
    posture_style: str = "natural"
    head_movement_style: str = "natural"
    eye_movement_style: str = "natural"

    preferred_gestures: list[str] = Field(default_factory=list)
    avoided_gestures: list[str] = Field(default_factory=list)

    movement_notes: str | None = None


class PersonProfile(BaseModel):
    """Persistent digital-human identity profile."""

    person_id: str
    display_name: str

    movement: MovementProfile

    voice_profile: str | None = None
    face_profile: str | None = None

    expression_style: str = "natural"
    speaking_style: str = "natural"