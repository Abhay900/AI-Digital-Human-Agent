from app.agents.script_analyzer import ScriptAnalyzer
from app.agents.video_planner import VideoPlanner
from app.core.person_profile import PersonProfile, MovementProfile


script = "A presenter explains why planning is important."

person = PersonProfile(
    person_id="person_001",
    display_name="Demo Person",
    movement=MovementProfile(
        gesture_style="controlled",
        hand_movement_style="measured hand gestures",
        body_movement_style="subtle body movement",
        movement_speed="moderate",
    ),
    expression_style="confident and informative",
)

analyzer = ScriptAnalyzer()
analysis = analyzer.analyze(script)

planner = VideoPlanner()
plan = planner.create_plan(analysis, person)

print("SCRIPT ANALYSIS")
print(analysis)

print("\nPERSON PROFILE")
print(person)

print("\nVIDEO PLAN")
print(plan)