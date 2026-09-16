from pydantic import BaseModel
from app.core.person_profile import PersonProfile


class VideoShot(BaseModel):
    shot_number: int
    scene_number: int
    duration_seconds: float
    camera: str
    framing: str
    expression: str
    gesture: str
    dialogue: str


class VideoPlan(BaseModel):
    shots: list[VideoShot]


class VideoPlanner:
    """Converts script analysis into a video production plan."""

    def create_plan(
        self,
        analysis,
        person: PersonProfile,
    ) -> VideoPlan:
        return VideoPlan(
            shots=[
                VideoShot(
                    shot_number=1,
                    scene_number=1,
                    duration_seconds=5.0,
                    camera="Static",
                    framing="Medium shot",
                    expression=person.expression_style,
                    gesture=(
                        f"{person.movement.gesture_style}; "
                        f"{person.movement.hand_movement_style}; "
                        f"{person.movement.body_movement_style}; "
                        f"speed: {person.movement.movement_speed}"
                    ),
                    dialogue=analysis.script,
                )
            ]
        )