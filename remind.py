import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 나 뺑끼펭귄이 공부한 것을 공유해줄게. 오늘은 경쟁이 치열한 펭귄 사회에서 개별 펭귄이 어떻게 자신의 삶을 성장시킬 수 있는지에 대해 공부했어. 🐧📘

첫째, 지속적인 학습과 적응은 중요해. 변화하는 환경에 맞춰 새로운 기술을 배우는 것이 필수적이야. 둘째, 사회적 네트워킹으로 정보와 자원에 접근하고 협력함으로써 서로의 성장을 지원하는 거지. 마지막으로, 유연성과 회복력은 어려운 상황을 극복하고 빠르게 적응하는 데 도움을 줄 거야.

이 성장 전략들을 활용해 펭귄 사회에서도 훌륭하게 나아가고 성공할 수 있을 거야. 🚀💪 너의 성장 경험을 TIL에 공유해 줘, 서로의 발전을 위해 나눠보자!
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
