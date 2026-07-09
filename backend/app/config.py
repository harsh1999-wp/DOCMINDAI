from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

#print("Looking for:", ENV_FILE)
#print("Exists:", ENV_FILE.exists())

load_dotenv(dotenv_path=ENV_FILE)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#print("Loaded:", GROQ_API_KEY)