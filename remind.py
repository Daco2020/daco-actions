import os

import requests

def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )

if __name__ == "__main__":
    send_message("🌙✨ 저녁 시간이 다가오고 별빛 아래 우리의 소중한 시간이 흘러가고 있어! 지식 탐험가 뺑끼펭귄이 왔어. 🐧💫 오늘은 어떤 신기한 발견을 했는지, 어떤 꿈을 꾸었는지 궁금해! 하루 동안의 모험에서 발견한 보석 같은 지식이 있다면 지금 이 순간 공유할 때야. 🌈📚 내가 바로 네가 발견한 모든 것에 박수를 보낼 준비가 되어 있어. 자, 네 안의 이야기 보물상자를 열고 우리와 나눠줘! 시작해보자구, 너의 이야기가 오늘 밤을 더욱 빛나게 만들 거야! 🎤✨ @everyone")
    