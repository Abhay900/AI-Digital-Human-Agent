from app.agents.script_analyzer import ScriptAnalyzer
from app.agents.video_planner import VideoPlan, VideoPlanner
from app.core.person_profile import PersonProfile


class AgentOrchestrator:
    """Coordinates the AI digital human production pipeline."""

    def __init__(
        self,
        script_analyzer: ScriptAnalyzer | None = None,
        video_planner: VideoPlanner | None = None,
    ):
        self.script_analyzer = script_analyzer or ScriptAnalyzer()
        self.video_planner = video_planner or VideoPlanner()

    def create_video_plan(
        self,
        script: str,
        person: PersonProfile,
    ) -> VideoPlan:
        """Analyze the script with the person profile and create a video plan."""

        analysis = self.script_analyzer.analyze(
            script=script,
            person=person,
        )

        return self.video_planner.create_plan(
            analysis=analysis,
            person=person,
        )