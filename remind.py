import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 오늘 뺑끼펭귄은 남극의 별들을 쳐다보며 우주에 대해 생각해봤어. 🌌🐧 그리고 내가 깨달은 건, 우리가 매일 배우는 작은 지식들도 이 거대한 우주의 한 부분이라는 거야! 앗, 좋은 생각이 났어! 🤭 오늘 우리의 TIL을 올리고, 여기에 별 이모지를 달면 어떨까? 🌟

이렇게 우리 각자의 배움이 모여 큰 지식의 우주를 만든다고 생각해봐. 너의 오늘 배운 것이 정말 궁금해! 별 이모지와 함께 너의 이야기를 나눠줘! 🌟📚
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
