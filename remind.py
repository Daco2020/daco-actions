import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
오늘 나는 얼음 위에서 새로운 미끄럼 기술을 발견했어! 🐧💨 바로 '초고속 뒤로 미끄러지기'라고 해. 한 번 시작하면 멈출 수 없어서, 펭귄들 사이에서는 이미 유행 중이지.

이제 너 차례야! 오늘 배운 가장 멋진 게 뭐야? 말 안 해주면 나 킹받을 거야, 빨리빨리 공유해봐! 📚✨ 그리고 매일 새로운 걸 배우는 너를 보는 건 정말 대박이야. 계속해서 지식의 바다에서 놀아보자고! 🌊🚀
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
