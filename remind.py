import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """🌟🐧 안녕! 뺑끼펭귄이야. 오늘 배운 건 '인내심'이야. 모든 성장은 시간이 필요하단 걸 깨달았어. 🕰️💡 너는 오늘 무엇을 배웠니? 작은 발걸음이라도 공유해줘. 너의 성장 과정이 궁금하거든!

기억해, 배움은 도전이야. 하지만, 그 속에서 우리는 더 강해져. 🌱🚀 너의 이야기, 듣고 싶어! 💌💬"""

if __name__ == "__main__":
    send_message(message + " @everyone")
