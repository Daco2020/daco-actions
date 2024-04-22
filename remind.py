import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 오늘의 TIL을 아직 안 올렸다면 지금 좋은 시간이야. 🐧📘 매일 배운 것을 공유하는 건 우리 모두에게 정말 큰 도움이 된단다. 네가 오늘 배운 흥미로운 것이든, 작은 발견이든, 모두 궁금해! 서로의 경험을 나눔으로써 우리 모두 더 많이 배울 수 있어. 그러니까, 언제든지 네 지식을 나와 공유해봐. 너의 이야기를 기다리고 있을게! 🌟✨
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
