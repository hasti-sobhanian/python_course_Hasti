import requests
import os
import dotenv
dotenv.load_dotenv()
from time import sleep



whatsapp_password = "ahdydjhfb23"
whatsapp_token = "1ddf324123"
BOT_TOKEN = os.getenv("telegram_token")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not set. Please check your .env file.")

CHAT_ID = "-1002830405443"

my_list = ["Hello", "My", "Name", "Is", "Hasti"]
MESSAGE = my_list

for i in range(len(my_list)):
    MESSAGE = f"message: {my_list[i]}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message:", response.text)
    sleep(2)  # Sleep for 2 second before sending the next message