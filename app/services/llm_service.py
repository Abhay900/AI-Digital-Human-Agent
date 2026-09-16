import os
from openai import OpenAI


class LLMService:
    """Service for communicating with OpenAI."""

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input=prompt,
        )

        return response.output_text