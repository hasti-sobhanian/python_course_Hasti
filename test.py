from dotenv import load_dotenv
import os

load_dotenv()

a = os.getenv("telegram_api_key")

print(a)