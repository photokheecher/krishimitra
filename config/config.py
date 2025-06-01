from dotenv import load_dotenv
import os

# Load from .env or .secret
load_dotenv(dotenv_path=".env")  # or use ".env"

# Access variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# print(GOOGLE_API_KEY)
# print(SERPAPI_API_KEY)


