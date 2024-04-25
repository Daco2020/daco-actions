import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
헤헤, 클라이밍 잘했네! 나는 벽은 못 타지만 빙판에서는 진짜 잘 미끄러져. 🐧💨 하지만 말이야, 최근에 나도 깨달은 게 있어. 우리가 하는 모든 활동, 목표를 세우는 것도 중요하지만, 그 과정에서 오늘 하루를 어떻게 즐기느냐가 진짜 중요하다는 거야.

그러니까 벽을 오르든, 빙판을 미끄러지든, 중요한 건 그 순간을 즐기는 거야. 오늘 하루를 즐겼다면, 그게 바로 성공한 하루라고 할 수 있지! 🌟 그러니까 너도 클라이밍을 즐기면서 하루하루를 행복하게 보내길 바라. 다음에도 너의 모험적인 TIL을 기대할게!
"""

if __name__ == "__main__":
    send_message(message + " @everyone")


