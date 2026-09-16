from pydantic import BaseModel


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

    def create_plan(self, analysis) -> VideoPlan:
        return VideoPlan(
            shots=[
                VideoShot(
                    shot_number=1,
                    scene_number=1,
                    duration_seconds=5.0,
                    camera="Static",
                    framing="Medium shot",
                    expression="Confident, informative",
                    gesture="Person-specific natural gesture",
                    dialogue=analysis.script,
                )
            ]
        )