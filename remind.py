import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
오늘 나는 바람의 방향과 속도가 날씨를 예측하는 데 얼마나 중요한지 배웠어! 🌬️🐧 바람을 관찰함으로써, 날씨 변화를 앞서 알 수 있다니, 정말 놀랍지 않아? 이제 내가 너에게 궁금한 건, 너희가 일상에서 날씨를 예측하거나 준비하는 데 어떤 기술이나 도구를 사용하는지야. 예를 들어, 가장 신뢰하는 날씨 앱이 뭐야?
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
