import os

import requests

def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )

if __name__ == "__main__":
    send_message("🌟🐧 어둠이 내려앉고 별이 반짝이는 밤이 왔어! 오, 지식의 모험가여, 오늘 네가 발견한 보물은 무엇인가요? ✨ 내 말이야, 오늘 하루 새롭게 알게 된 것들! 📖💫 지금이 바로 그 귀중한 이야기들을 나와 함께 나눌 시간이란다. 걱정 말고, 마음을 열고 너의 이야기를 펼쳐봐. 내가 여기서 너의 모든 이야기에 귀 기울일게. 자, 그럼 우리의 오늘을 빛낼 이야기들을 시작해볼까? 🎉📚 @everyone")
    