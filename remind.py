import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
어맛? 벌써 10시네! 설마 아직 TIL을 올리지 않은 친구들이 있을까? 🐧🕙 걱정 마, 아직 2시간이나 남았어! 이 시간 동안 집중해서 멋진 지식을 나눠보자구!

TIL을 이미 올린 친구들은 🍄 이모지를 남겨봐! 보고만 있어도 기분이 좋아질 거야, 헤헤. 🌟📘
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
