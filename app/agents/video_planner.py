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
    """Converts script analysis into a digital human video plan."""

    def create_plan(
        self,
        analysis,
        person: PersonProfile,
    ) -> VideoPlan:

        video_shots = []

        for shot in analysis.shots:
            gesture = (
                f"{shot.gesture}; "
                f"Person style: {person.movement.gesture_style}; "
                f"Hand movement: {person.movement.hand_movement_style}; "
                f"Body movement: {person.movement.body_movement_style}; "
                f"Movement speed: {person.movement.movement_speed}"
            )

            video_shots.append(
                VideoShot(
                    shot_number=shot.shot_number,
                    scene_number=shot.scene_number,
                    duration_seconds=shot.duration_seconds,
                    camera=shot.camera,
                    framing=shot.framing,
                    expression=shot.expression,
                    gesture=gesture,
                    dialogue=shot.dialogue,
                )
            )

        return VideoPlan(shots=video_shots)