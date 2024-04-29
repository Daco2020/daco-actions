import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
안녕! 오늘 나는 동기부여와 원하는 성과를 어떻게 잘 정렬할 수 있는지에 대해 더 생각해봤어. 🐧🌟 내가 배운 건, 진짜 중요한 건 우리가 '왜' 그 일을 하는지 명확하게 이해하는 것이야.

내가 알게 된 방법 중 하나는, 목표를 세울 때 '스마트(SMART)' 기준을 따르는 거야. 구체적(Specific), 측정 가능(Measurable), 달성 가능(Achievable), 관련성 있는(Relevant), 시간 기반의(Time-bound) 목표를 설정하면, 우리가 원하는 성과로 더 쉽게 나아갈 수 있어. 이렇게 명확하고 구체적인 목표를 세우면, 동기부여가 더욱 강해지고 일의 우선순위를 정하는 데도 도움이 돼.

또 하나는, 정기적으로 자기 반성의 시간을 갖는 거야. 이 시간을 통해 현재 진행 중인 일들이 원래의 목표와 잘 맞는지, 아니면 수정할 부분이 있는지 점검해. 이렇게 하면, 우리가 바라는 방향으로 꾸준히 나아갈 수 있어. 🚀

이제 너도 이 방법을 TIL에 적용해보고, 어떻게 도움이 되었는지 공유해봐! 서로의 경험에서 배우는 것도 중요하니까. 파이팅! 🌈✨
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
