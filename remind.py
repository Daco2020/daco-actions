import os

import requests

def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )

if __name__ == "__main__":
    send_message("🐧✨ 빛나는 밤이 찾아왔네! 그 말인즉슨, 오늘 하루 배운 걸 공유할 시간이라는 거야. 🌙✨ 내가 바로 지식의 보고, 뺑끼펭귄! 오늘도 우리의 뇌세포들을 깨워볼까? 🧠💡 마음의 창고를 열고 오늘 얻은 보물들을 나눠봐. 걱정 마, 내가 다 들어줄게. 그래, 시작해볼까? 📚💖 @everyone")
    