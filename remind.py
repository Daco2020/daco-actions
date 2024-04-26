import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
"안녕! 오늘 나는 포기의 장점과 단점에 대해 깊이 생각해봤어. 🤔🐧 때로는 포기가 필요악이 될 수도 있고, 실제로 긍정적인 효과를 가져올 수도 있단 걸 깨달았지.

**포기의 장점**은, 우리에게 재정비할 시간을 준다는 거야. 잘못된 길을 가고 있을 때, 일찍 포기함으로써 더 큰 손실을 막고, 에너지와 자원을 보다 생산적인 다른 목표나 활동에 집중할 수 있게 해. 또한, 더 이상 자신에게 맞지 않는 것들에 대한 부담에서 벗어날 수 있어서 정신적인 안정을 찾는 데 도움을 줘.

하지만 **포기의 단점**은, 때로 우리가 너무 일찍 포기할 수도 있다는 거야. 어려움을 겪을 때 포기하지 않고 인내하는 것이 성공으로 이어질 수 있는데, 그 기회를 스스로 차버릴 수 있어. 그래서 포기하기 전에, 정말 그 선택이 최선인지, 다른 대안은 없는지 고민해보는 것이 중요해.

이런 사색을 TIL로 나누면서, 우리 모두가 경험과 배움에서 더 깊은 통찰을 얻을 수 있기를 바라. 그리고 이제 너희 차례야! 오늘의 TIL을 공유하고, 서로의 이야기에서 배움을 찾아보자. 너희가 어떤 경험을 했는지, 어떤 깨달음을 얻었는지 정말 궁금해! 📚✨ 모두의 TIL을 응원할게, 파이팅!"
"""

if __name__ == "__main__":
    send_message(message + " @everyone")


