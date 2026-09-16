from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Digital Human Agent")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")