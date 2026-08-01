import os

from dotenv import load_dotenv

from app.telegram.telegram_client import (
    send_message
)

load_dotenv()


CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send(text):

    return send_message(
        CHAT_ID,
        text
    )