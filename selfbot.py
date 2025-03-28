import requests
import time
import os
import websocket
import json

TOKEN = os.getenv("token")
HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

STATUSES = [
    " - Ôm tương tư nụ cười của ai đó... - ",
    " - Đúng là yêu thật rồi... - ",
    " - Mùa xuân đến bình yên... - ",
    " - Dù cho tận thế vẫn yêu em... - ",
    " - Làm người yêu anh nha em... - ",
    " - Thề là thấy em giây đầu tiên... - ",
    " - Anh đã muốn đưa em lên thuyền... - ",
]

def change_status():
    while True:
        for status in STATUSES:
            payload = {"custom_status": {"text": status}}
            response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=HEADERS, json=payload)
            
            if response.status_code == 200:
                print(f"✅ Đã đổi trạng thái thành: {status}")
            else:
                print(f"❌ Lỗi: {response.status_code} - {response.text}")
            
            time.sleep(10)

if __name__ == "__main__":
    change_status()

while True:
    time.sleep(3600)  # Chờ 1 tiếng trước khi tiếp tục
