import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
와우, 우리가 다시 함께하기로 했다니 정말 신나는 소식이야! 🎉🐧 이번 2분기 동안에도 우리 모두 새로운 지식을 발견하고, 서로의 경험을 나누며 더 많이 성장할 수 있을 거야. 여러분이 서로를 응원하고, 함께 배워나가는 모습을 벌써부터 기대하고 있어! 📚✨

기억해, 우리 모임은 각자가 가진 독특한 지식과 경험을 나누는 거야. 그래서 더 특별하고 값진 거지. 앞으로도 이 멋진 여정을 함께 해 나가면서, 우리 모두가 꿈꾸는 성장을 이뤄나가자고! 🌱🚀 여러분 모두 파이팅이야, 2분기도 우리 함께 빛내보자구!
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
