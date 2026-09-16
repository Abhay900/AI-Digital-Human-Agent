from pydantic import BaseModel


class Scene(BaseModel):
    scene_number: int
    description: str


class Shot(BaseModel):
    shot_number: int
    scene_number: int
    description: str
    camera: str


class ScriptAnalysis(BaseModel):
    script: str
    scenes: list[Scene]
    shots: list[Shot]
    dialogue: list[str]
    expressions: list[str]
    gestures: list[str]


class ScriptAnalyzer:
    """Analyzes a script and prepares it for video planning."""

    def analyze(self, script: str) -> ScriptAnalysis:
        return ScriptAnalysis(
            script=script,
            scenes=[
                Scene(
                    scene_number=1,
                    description="Presenter explains why planning is important."
                )
            ],
            shots=[
                Shot(
                    shot_number=1,
                    scene_number=1,
                    description="Presenter speaking directly to camera.",
                    camera="Medium shot, eye-level"
                )
            ],
            dialogue=[script],
            expressions=["Confident, informative"],
            gestures=["Natural hand gestures while explaining"],
        )