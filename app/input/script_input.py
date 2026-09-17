class ScriptInput:
    """Handles and validates user-provided video scripts."""

    def clean(self, script: str) -> str:
        if not isinstance(script, str):
            raise TypeError("Script must be a string.")

        cleaned_script = script.strip()

        if not cleaned_script:
            raise ValueError("Script cannot be empty.")

        return cleaned_script
    