import os

import requests

def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )

if __name__ == "__main__":
    a = send_message("오늘 하루 배운 것을 올려보아요!🤓 @everyone")