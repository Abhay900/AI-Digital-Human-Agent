class LLMService:
    """Base service for communicating with an AI language model."""

    def generate(self, prompt: str) -> str:
        raise NotImplementedError(
            "LLM provider has not been connected yet."
        )