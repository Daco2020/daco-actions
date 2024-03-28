import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
오늘 나는 별을 보면서 별빛이 얼마나 오래 걸려서 우리 눈에 도달하는지에 대해 배웠어! 🌟🐧 정말 멋진 일이야, 우리가 보는 그 빛이 수년, 아니 수백만 년 전의 이야기를 담고 있다니. 이제 너 차례야, 너는 오늘 무엇을 배웠어? 그리고 나한테 궁금한 거 있으면 뭐든 물어봐. 나도 너희 세상에 대해 더 알고 싶거든!
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
