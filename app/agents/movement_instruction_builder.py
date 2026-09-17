from app.core.person_profile import PersonProfile


class MovementInstructionBuilder:
    """Builds person-specific movement instructions for video generation."""

    def build(self, person: PersonProfile) -> str:
        movement = person.movement

        instructions = [
            "Follow the authorized person's personal movement profile.",
            f"Gesture style: {movement.gesture_style}.",
            f"Hand movement: {movement.hand_movement_style}.",
            f"Body movement: {movement.body_movement_style}.",
            f"Movement speed: {movement.movement_speed}.",
            f"Gesture frequency: {movement.gesture_frequency}.",
            f"Posture: {movement.posture_style}.",
            f"Head movement: {movement.head_movement_style}.",
            f"Eye movement: {movement.eye_movement_style}.",
        ]

        if movement.preferred_gestures:
            instructions.append(
                "Preferred gestures: "
                + ", ".join(movement.preferred_gestures)
                + "."
            )

        if movement.avoided_gestures:
            instructions.append(
                "Avoid these gestures: "
                + ", ".join(movement.avoided_gestures)
                + "."
            )

        if movement.movement_notes:
            instructions.append(
                f"Additional movement notes: {movement.movement_notes}"
            )

        return " ".join(instructions)