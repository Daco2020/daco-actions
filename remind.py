import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
하이! 오늘 나, 뺑끼펭귄은 남극에서 별이 얼마나 밝게 빛나는지 관찰했어. 🌌🐧 별들 사이를 날아다니는 것 같은 느낌이었지. 상상만으로도 짜릿하잖아?

이제 너의 차례야! TIL에서 오늘 배운 멋진 걸 공유해봐. 말 안 하면 나 정말 심심해질 거야, 그러니까 얼른 얼른! 📘✨ 네가 매일 새로운 지식을 쌓아가는 걸 보는 게 정말 멋지다고 생각해. 계속해서 꾸준히 해나가보자, 파이팅! 너도 할 수 있어! 🚀💪
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
