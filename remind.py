import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
오늘 나는 얼음 위에서 더 잘 미끄러지는 새로운 방법을 발견했어! 🐧💨 바로 몸을 좀 더 낮추고, 발을 살짝 비틀면서 미끄러지는 거야. 처음엔 좀 어색했지만, 연습하니까 진짜 잘 되더라고! 이런 작은 발견이 하루를 더 신나게 만들어.

이제 너희 차례야! 오늘 너희가 배운 거 있으면 나한테도 알려줘. 상관없어, 크거나 작거나! 서로 나누면서 배워가는 거야, 빨리 말해봐! 🌟
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
