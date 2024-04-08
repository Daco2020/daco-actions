import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
야호! 드디어 새로운 시작, 1일차 TIL 인증의 시간이 왔어! 🎉🐧 우리 모두가 서로에게 배울 준비가 되어 있는지 확인하는 첫걸음이니까 정말 중요해. 오늘 배운 것, 아무리 작은 것이라도 좋으니까 망설이지 말고 공유해봐. 이게 바로 우리가 함께 성장해 나가는 방법이야! 📚💡

기억해, 이 작은 시작이 우리 모두에게 큰 변화를 가져다 줄 거야. 오늘 배운 것을 인증하고, 그 과정에서 느낀 점, 궁금한 점들을 나눠보자고. 서로의 경험에서 배우고, 함께 더 나은 내일을 만들어 가는 거야. 🌟🐧

그럼, 1일차 TIL 인증, 시작해볼까? 너의 이야기를 기다리고 있을게!
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
