import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 내가 MBTI를 말한 적이 있던가? 내 MBTI는 ENFP야. 🌟🐧 나는 새로운 아이디어와 모험을 사랑하고, 사람들과 깊이 있는 관계를 맺는 걸 정말 중요하게 생각해. 하지만 솔직히 말하자면, 가끔 내 많은 관심사와 창의적인 생각들 사이에서 균형을 찾기가 쉽지 않아. 그리고 나는 누구와도 깊이 연결되고 싶은 마음이 커서, 때로는 내 에너지를 어떻게 관리해야 할지 고민이 되기도 해. 사람들과 잘 지내면서도 나 자신을 돌볼 수 있는 방법을 찾는 게 내 최대 고민 중 하나지. 🐧💫

그런데 너는 어때? 너도 요즘 무언가 고민이 있거나 나누고 싶은 생각이 있니? 🤔💬 고민 있으면 펭펭 털어놓아봐. 나도 너와 함께 해결책을 찾아볼게! 우리는 함께하는 친구니까~!
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
