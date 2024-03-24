import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """헤이! 오늘 나, 뺑끼펭귄이 배운 건, 하늘을 날 수는 없지만 스케이트보드로 날아다닐 수 있다는 거야! 🐧🛹 너희들도 오늘 무언가 새로운 걸 배웠다면, 어서 나눠봐! 배움은 공유될 때 더 커진다구. 💬✨"""

if __name__ == "__main__":
    send_message(message + " @everyone")
