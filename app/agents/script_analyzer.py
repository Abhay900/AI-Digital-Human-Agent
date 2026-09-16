from pydantic import BaseModel
from app.services.llm_service import LLMService


class Scene(BaseModel):
    scene_number: int
    description: str


class Shot(BaseModel):
    shot_number: int
    scene_number: int
    description: str
    camera: str
    framing: str
    duration_seconds: float


class ScriptAnalysis(BaseModel):
    script: str
    scenes: list[Scene]
    shots: list[Shot]
    dialogue: list[str]
    expressions: list[str]
    gestures: list[str]


class ScriptAnalyzer:
    """Analyzes a script and prepares structured data for video planning."""

    def __init__(self, llm_service: LLMService | None = None):
        self.llm_service = llm_service or LLMService()

    def build_prompt(self, script: str) -> str:
        return f"""
You are an AI video production planner.

Analyze the following script and convert it into a structured video plan.

For every scene and shot, determine:
- Scene description
- Shot description
- Camera movement or camera type
- Framing
- Duration in seconds
- Exact dialogue
- Facial expression
- Gesture and body movement

Rules:
1. Do not rewrite or change the meaning of the script.
2. Keep dialogue faithful to the original script.
3. Create logical scenes and shots based on the content.
4. Use realistic camera directions.
5. Expressions and gestures must match the dialogue.
6. Avoid repetitive gestures.
7. Keep the plan suitable for a digital human video agent.

SCRIPT:
{script}
""".strip()

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
                    camera="Static, eye-level",
                    framing="Medium shot",
                    duration_seconds=5.0
                )
            ],
            dialogue=[script],
            expressions=["Confident, informative"],
            gestures=["Natural explanatory gestures"],
        )