import requests
import time
import os
TOKEN = os.getenv("token")
HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

STATUSES = [
    "💗 - Từng ngày đều phải cố để luôn tươi cười -",
    "💗 - Trở thành một thằng ngáo ngơ -",
    "💗 - Anh ngáo ngơ vì em mà -",
    "💗 - Anh cứ đi trên con đường xưa khi ta bên nhau -"
]

def check_connection():
    """Kiểm tra xem token có bị mất kết nối không"""
    ws = websocket.create_connection("wss://gateway.discord.gg/?v=9&encoding=json")
    ws.send(json.dumps({"op": 2, "d": {"token": TOKEN, "properties": {}}}))
    response = ws.recv()
    ws.close()
    return "ready" in response

def change_status():
    while True:
        if check_connection():
            for status in STATUSES:
                payload = {"custom_status": {"text": status}}
                response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=HEADERS, json=payload)
                if response.status_code == 200:
                    print(f"✅ Đã đổi trạng thái thành: {status}")
                else:
                    print(f"❌ Lỗi: {response.status_code} - {response.text}")
                time.sleep(10)
        else:
            print("⚠️ Mất kết nối! Chờ 10s để thử lại...")
            time.sleep(3)

if __name__ == "__main__":
    change_status()

while True:
    time.sleep(3600)  # Chờ 1 tiếng trước khi tiếp tục
