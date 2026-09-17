import json

from pydantic import BaseModel

from app.core.person_profile import PersonProfile
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
    """Analyzes a script using the person's digital-human profile."""

    def __init__(
        self,
        llm_service: LLMService | None = None,
        use_mock: bool = True,
    ):
        self.llm_service = llm_service or LLMService()
        self.use_mock = use_mock

    def build_prompt(
        self,
        script: str,
        person: PersonProfile | None = None,
    ) -> str:

        person_context = ""

        if person:
            movement = person.movement

            person_context = f"""
AUTHORIZED PERSON MOVEMENT PROFILE:
- Gesture style: {movement.gesture_style}
- Hand movement: {movement.hand_movement_style}
- Body movement: {movement.body_movement_style}
- Movement speed: {movement.movement_speed}
- Gesture frequency: {movement.gesture_frequency}
- Posture: {movement.posture_style}
- Head movement: {movement.head_movement_style}
- Eye movement: {movement.eye_movement_style}
- Preferred gestures: {", ".join(movement.preferred_gestures) or "None specified"}
- Avoided gestures: {", ".join(movement.avoided_gestures) or "None specified"}
- Movement notes: {movement.movement_notes or "None"}
"""

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

PERSON-SPECIFIC RULES:
1. Treat the authorized person's movement profile as a constraint.
2. Prefer the person's natural movement characteristics.
3. Use preferred gestures when appropriate.
4. Avoid gestures listed as avoided gestures.
5. Do not invent exaggerated or unnatural movements.
6. Match gestures and expressions to the dialogue.
7. Keep movements realistic and purposeful.

{person_context}

GENERAL RULES:
1. Do not rewrite or change the meaning of the script.
2. Keep dialogue faithful to the original script.
3. Divide the script into logical scenes and shots.
4. Avoid repetitive gestures.
5. Use realistic camera directions.
6. Keep the plan suitable for a digital human video.
7. Every shot must contain its own dialogue, expression and gesture.
8. Return only valid JSON matching the required schema.

SCRIPT:
{script}
""".strip()

    def parse_response(self, response: str) -> ScriptAnalysis:
        """Convert an AI response into a validated ScriptAnalysis object."""

        try:
            data = json.loads(response)
        except json.JSONDecodeError as exc:
            raise ValueError("AI response is not valid JSON.") from exc

        return ScriptAnalysis.model_validate(data)

    def analyze(
        self,
        script: str,
        person: PersonProfile | None = None,
    ) -> ScriptAnalysis:

        script = script.strip()

        if not script:
            raise ValueError("Script cannot be empty.")

        if self.use_mock:
            return self._mock_analysis(script, person)

        prompt = self.build_prompt(
            script=script,
            person=person,
        )

        response = self.llm_service.generate(prompt)

        return self.parse_response(response)

    def _mock_analysis(
        self,
        script: str,
        person: PersonProfile | None = None,
    ) -> ScriptAnalysis:

        gesture = "Natural explanatory gestures"

        if person:
            gesture = (
                f"Use {person.movement.gesture_style} gestures "
                f"with {person.movement.hand_movement_style}."
            )

        return ScriptAnalysis(
            script=script,
            scenes=[
                Scene(
                    scene_number=1,
                    description="Presenter introduces the main message.",
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
                    expression="Confident and informative",
                    gesture=gesture,
                )
            ],
        )