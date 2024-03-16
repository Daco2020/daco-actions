import os

import requests

def send_message(message: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        os.environ["DISCORD_WEBHOOK_URL"],
        data={"content": message},
    )

if __name__ == "__main__":
    send_message("🌌💖 밤의 별빛이 찬란하게 우리를 비추는군요, 지식의 여행자여! 뺑끼펭귄이 말하네, 오늘 네가 겪은 모험에서 얻은 교훈은 무엇인가요? 📖✨ 작은 깨달음부터 큰 영감에 이르기까지, 모든 것이 귀중해요. 이제, 그 소중한 순간들을 우리와 공유할 시간이에요. 🌟💌 용기 내어 너의 이야기를 펼쳐보세요. 이곳은 너의 생각과 경험을 나누며 함께 성장할 수 있는 공간이랍니다. 자, 너의 이야기로 이 밤을 더욱 빛나게 만들어 봐요! 🚀✨ @everyone")
    