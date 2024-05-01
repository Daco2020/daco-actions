import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 오늘은 자기혐오에 빠지지 않는 방법 중 하나를 공유하고 싶어. 🐧💡 가끔 우리는 스스로를 너무 엄격하게 평가하며 '나는 충분히 잘하고 있지 않아'라고 느낄 때가 있어. 이럴 때 **자기 돌봄(Self-care)**이 정말 중요해.

자기 돌봄은 스스로에게 친절하게 대하는 법을 배우는 거야. 간단한 명상, 좋아하는 책 읽기, 산책 등 자신이 좋아하고 편안해지는 활동을 통해 마음의 여유를 갖는 거지. 이런 작은 행동들이 너를 더 긍정적으로 만들고, 스스로를 혹독하게 대하는 순간들을 줄일 수 있어.

그러니까 오늘부터라도 자기 자신에게 조금 더 친절하자구! 너는 이미 충분히 멋지고, 가치 있는 사람이야. 네가 스스로에게 주는 사랑과 관심이 결국 너를 더욱 강하고 행복하게 만들 거야. 파이팅! 🌟✨
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
