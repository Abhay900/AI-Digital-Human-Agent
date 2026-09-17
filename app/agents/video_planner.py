from pydantic import BaseModel

from app.agents.movement_instruction_builder import MovementInstructionBuilder
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
    """Converts script analysis into a person-aware digital human video plan."""

    def __init__(
        self,
        movement_builder: MovementInstructionBuilder | None = None,
    ):
        self.movement_builder = (
            movement_builder or MovementInstructionBuilder()
        )

    def create_plan(
        self,
        analysis,
        person: PersonProfile,
    ) -> VideoPlan:

        movement_instructions = self.movement_builder.build(person)

        video_shots = []

        for shot in analysis.shots:
            gesture = (
                f"Shot gesture: {shot.gesture}. "
                f"{movement_instructions}"
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