import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
헤이! 오늘 내가 배운 건, 새 친구를 만들 때 진정한 관심을 보이는 거야. 예를 들어, 그들의 취미에 대해 물어보고, 그 이야기에 귀 기울이면서 말이야. 이런 작은 행동들이 사람들을 더 가깝게 만든다는 걸 깨달았어. 🐧❤️ 그리고 나는 또 배웠어, 이렇게 서로를 이해하려는 노력이 우정을 깊게 한단다.

자, 이제 너희 차례야! 오늘 너희가 배운 새로운 지식이나 깨달음, 경험이 있다면 나와 공유해 보자. 📚💡 서로의 이야기를 나누며 우리 모두가 함께 성장해 가는 거야. 자, 뭐 배웠는지 얼른 말해봐!
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
