from app.agents.orchestrator import AgentOrchestrator
from app.core.person_profile import PersonProfile, MovementProfile


script = "A presenter explains why planning is important."


person = PersonProfile(
    person_id="person_001",
    display_name="Demo Person",
    movement=MovementProfile(
        gesture_style="controlled and confident",
        hand_movement_style="measured open-palm gestures",
        body_movement_style="subtle upper-body movement",
        movement_speed="moderate",
        gesture_frequency="moderate",
        posture_style="upright and relaxed",
        head_movement_style="subtle nods while emphasizing points",
        eye_movement_style="natural direct-to-camera focus",
        preferred_gestures=[
            "open palm",
            "small explanatory hand movement",
            "subtle nod",
        ],
        avoided_gestures=[
            "excessive waving",
            "rapid hand movements",
            "large unnecessary body movements",
        ],
        movement_notes=(
            "Keep gestures purposeful, natural and restrained. "
            "Movement should support the dialogue rather than distract from it."
        ),
    ),
    expression_style="confident and informative",
    speaking_style="clear, professional and conversational",
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