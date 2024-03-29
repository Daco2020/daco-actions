import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
오늘이 우리의 마지막 TIL 이야! 🐧✨ 이 한 달 동안 진짜 잘해줬어, 모두 고생 많았어. 서로 배우고 나눈 거, 정말 멋졌다고. 4월에도 다시 만나서 이야기 많이 나누자, 알았지? 그때까지 모두 건강하게 지내고, 다음에 또 보자고, 약속! 🌼💪
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
