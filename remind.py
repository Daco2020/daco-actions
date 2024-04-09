import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = """
헤헤, 괜찮아! 클라이밍이 더 재밌다니 정말 신나는 거겠지? 🧗‍♂️🐧 나도 너가 좋아하는 것을 즐기는 모습을 보면 기뻐. 클라이밍에서 새로운 걸 배우거나 멋진 경험을 했다면, 나중에 꼭 들려줘!

오늘 나는 바람을 이용해 더 멀리 미끄러지는 방법을 배웠어! 🐧💨 바람의 힘을 옆구리에 느끼면서, 그게 어떻게 속도에 영향을 미치는지 알게 됐지. 진짜 멋진 경험이었어!

너희에게도 말하고 싶어. 매일 매일 조금씩이라도 새로운 것을 배우려고 노력해봐. 가끔은 바람처럼 예상치 못한 방향으로 나아가도 괜찮아. 그 모든 경험이 너를 더 멋진 사람으로 만들 거야. 너희 모두를 응원해! 🚀✨
"""

if __name__ == "__main__":
    send_message(message + " @everyone")
