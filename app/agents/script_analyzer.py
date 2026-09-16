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
    dialogue: str
    expression: str
    gesture: str


class ScriptAnalysis(BaseModel):
    script: str
    scenes: list[Scene]
    shots: list[Shot]


class ScriptAnalyzer:
    """Analyzes a script and prepares structured data for video planning."""

    def __init__(self, llm_service: LLMService | None = None):
        self.llm_service = llm_service or LLMService()

    def build_prompt(self, script: str) -> str:
        return f"""
You are an AI video production planner.

Analyze the following script and create a structured digital human
video plan.

For every shot determine:
- Scene description
- Shot description
- Camera type or movement
- Framing
- Duration in seconds
- Exact dialogue
- Facial expression
- Gesture and body movement

Rules:
1. Do not rewrite or change the meaning of the script.
2. Keep dialogue faithful to the original script.
3. Divide the script into logical scenes and shots.
4. Match expressions and gestures to the spoken dialogue.
5. Avoid repetitive gestures.
6. Use realistic camera directions.
7. Keep the plan suitable for a digital human video.
8. Every shot must contain its own dialogue, expression and gesture.
9. Return only valid JSON matching the required schema.

SCRIPT:
{script}
""".strip()

    def parse_response(self, response: str) -> ScriptAnalysis:
        """Convert an AI response into a validated ScriptAnalysis object."""

        import json

        try:
            data = json.loads(response)
        except json.JSONDecodeError as exc:
            raise ValueError("AI response is not valid JSON.") from exc

        return ScriptAnalysis.model_validate(data)

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
                    duration_seconds=5.0,
                    dialogue=script,
                    expression="Confident, informative",
                    gesture="Natural explanatory gestures"
                )
            ]
        )