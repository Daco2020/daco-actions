import os

import requests


def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )


message = "🐧✨ 오호라, 내 차례가 되었군! 오늘 내가 배운 건, 별빛도 우리의 이야기를 듣고 싶어 한다는 거야. 🌌🌠 그래서 나도 너에게 배운 것을 공유할게. 바로, 친구와 지식을 나누면 그 즐거움이 두 배가 된다는 사실! 📖➕📖=💖 이제 네 차례야, 친구야. 오늘 네가 배운 건 뭐야? 내가 먼저 나눴으니, 너도 나와 나눠줘. 🎤👀 기다리고 있을게, 헤헷!"

if __name__ == "__main__":
    send_message(message + " @everyone")
