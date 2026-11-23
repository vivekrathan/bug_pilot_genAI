
from google import genai
from app.config import settings

client = genai.Client(api_key=settings.gemini_api_key)

models = [
    "gemini-3.8-flash",
    "gemini-3.5-flash-lite",
]

for model in models:
    print(f"\nTesting model: {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Reply with only: Gemini is working."
        )

        print("SUCCESS:", response.text)

    except Exception as error:
        print("FAILED:", type(error).__name__)
        print("DETAIL:", error)
