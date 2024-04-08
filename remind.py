import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 오늘 나, 뺑끼펭귄은 남극의 해가 어떻게 한밤중에도 빛나는지 배웠어. 정말 신기하더라고! 🌞🐧 그리고 나는 너희 모두가 새로운 것을 배우고, 꾸준히 도전하는 걸 멈추지 않기를 바라.

기억해, 우리 모두가 서로 다른 길을 걷고 있을지라도, 매일 조금씩 배우며 나아가는 것이 중요해. 너희 모두가 가진 무한한 가능성을 믿어. 계속해서 도전하고, 배우고, 성장해 나가자! 파이팅! 🚀💖
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
