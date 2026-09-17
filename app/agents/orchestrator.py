from app.agents.movement_instruction_builder import MovementInstructionBuilder
from app.agents.script_analyzer import ScriptAnalyzer
from app.agents.video_planner import VideoPlan, VideoPlanner
from app.core.person_profile import PersonProfile
from app.input.script_input import ScriptInput


class AgentOrchestrator:
    """Coordinates the AI digital human production pipeline."""

    def __init__(
        self,
        script_input: ScriptInput | None = None,
        script_analyzer: ScriptAnalyzer | None = None,
        video_planner: VideoPlanner | None = None,
        movement_builder: MovementInstructionBuilder | None = None,
    ):
        self.script_input = script_input or ScriptInput()
        self.script_analyzer = script_analyzer or ScriptAnalyzer()
        self.movement_builder = (
            movement_builder or MovementInstructionBuilder()
        )
        self.video_planner = video_planner or VideoPlanner(
            movement_builder=self.movement_builder
        )

    def create_video_plan(
        self,
        script: str,
        person: PersonProfile,
    ) -> VideoPlan:
        """Validate the script and create a person-aware video plan."""

        cleaned_script = self.script_input.clean(script)

        analysis = self.script_analyzer.analyze(
            script=cleaned_script,
            person=person,
        )

        return self.video_planner.create_plan(
            analysis=analysis,
            person=person,
        )