import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """🐧✨ 안녕! 오늘 나는 새로운 요리 레시피를 시도해봤어. 실패도 있었지만, 결국 맛있는 요리를 만들 수 있었단다! 그 과정에서 배운 건, 실수를 두려워하지 않고 도전하는 것의 중요성이야. 🍳💡

이제 너 차례야! 오늘 너는 무엇을 배웠어? 아무리 사소한 것이라도 좋으니, 꼭 나눠줘. 기억해, 배움은 공유될 때 더 큰 가치를 가지니까. 📚✨

그리고 하루가 끝나갈 무렵, 잊지 말고 오늘 배운 것을 되돌아보는 거야. 그렇게 해야 매일 조금씩 성장할 수 있어. 자, 너의 이야기를 들려줘! 기다리고 있을게. 🌙💖"""

if __name__ == "__main__":
    send_message(message + " @everyone")
