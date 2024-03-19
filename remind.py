import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = "🐧🎈 헤헷, 야호! 밤이 됐어, 이제 뭐할 차례지? 맞아, 오늘 배운 것들을 나랑 나눠야 할 시간이야! 🌟📚 너의 소중한 발견들, 나도 궁금해 죽겠어. 얼른 얼른, 비밀스런 이야기 상자 열고 나와 함께 공유해볼까? 빨리빨리, 시간이 없어! 🏃💨"

if __name__ == "__main__":
    send_message(message + " @everyone")
