from app.agents.orchestrator import AgentOrchestrator
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


orchestrator = AgentOrchestrator()

video_plan = orchestrator.create_video_plan(
    script=script,
    person=person,
)


print("AI DIGITAL HUMAN AGENT")
print("\nPERSON PROFILE")
print(person)

print("\nVIDEO PLAN")
print(video_plan)