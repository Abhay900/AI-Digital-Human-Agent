from app.agents.script_analyzer import ScriptAnalyzer
from app.agents.video_planner import VideoPlanner


script = "A presenter explains why planning is important."

analyzer = ScriptAnalyzer()
analysis = analyzer.analyze(script)

planner = VideoPlanner()
plan = planner.create_plan(analysis)

print("SCRIPT ANALYSIS")
print(analysis)

print("\nVIDEO PLAN")
print(plan)