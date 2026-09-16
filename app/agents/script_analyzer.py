from pydantic import BaseModel
from app.services.llm_service import LLMService

class ScriptAnalyzer:
    """Analyzes a script and prepares structured data for video planning."""

    def __init__(self, llm_service: LLMService | None = None):
        self.llm_service = llm_service or LLMService()

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
    """Analyzes a script and prepares structured data for video planning."""

    def analyze(self, script: str) -> ScriptAnalysis:
        script = script.strip()

        if not script:
            raise ValueError("Script cannot be empty.")

        return ScriptAnalysis(
            script=script,
            scenes=[
                Scene(
                    scene_number=1,
                    description="Presenter explains the main message."
                )
            ],
            shots=[
                Shot(
                    shot_number=1,
                    scene_number=1,
                    description="Presenter speaks directly to camera.",
                    camera="Static, eye-level, medium shot"
                )
            ],
            dialogue=[script],
            expressions=["Confident, informative"],
            gestures=["Natural explanatory gestures"],
        )