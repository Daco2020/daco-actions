import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 나, 뺑끼펭귄이 아침에 일어나서 가장 먼저 하는 중요한 일은 바로 일기 쓰기야. 🐧📖 아침 일기를 통해 하루를 계획하고, 전날의 경험을 되돌아보며 감사할 점을 찾아. 이 작은 습관이 하루를 긍정적으로 시작하는 데 큰 도움이 되거든.

일기 쓰기는 하루를 명확하고 의도적으로 시작할 수 있게 해줘서, 내 목표에 집중하고 그날 그날을 최대한 의미 있게 보낼 수 있게 도와줘.

너도 아침 루틴에 이런 작은 습관을 하나 추가해보는 건 어때? 그리고 네가 아침에 새롭게 시작한 습관이 어떤 변화를 가져다주는지 TIL에 공유해봐! 네 경험이 다른 사람들에게도 영감을 줄 수 있을 거야. 파이팅! 🚀✨
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
