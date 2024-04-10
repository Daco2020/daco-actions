import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
헤헤, 고마워! 🐧💖 내가 귀엽다니, 너도 정말 귀여운 거 알아? 그런 너가 TIL에 참여해서 매일 새로운 걸 배우려고 하는 모습도 정말 멋져!

언제나 네가 배우고 싶은 것, 꿈꾸는 모든 것들을 향해 나아가길 응원할게. 🚀✨ TIL에서 오늘 배운 것들을 나누면서, 너의 지식과 경험이 더욱 풍부해지길 바라. 파이팅, 친구야! 너의 열정이 더 많은 발견으로 이끌어줄 거야. 🌟
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
