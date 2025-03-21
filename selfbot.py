import requests
import time
import os
TOKEN = os.getenv("token")
headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

statuses = [
    "💗 -- Nhớ em anh không thể nào cai --",
    "💗 -- Em xinh như một thiên thần --",
    "💗 -- Hình như trong lòng anh đã không còn hình bóng ai ngoài em đâu --",
    "💗 -- Dù cho tận thế vẫn yêu em luôn yêu em --",

]

while True:
    for status in statuses:
        status_data = {"custom_status": {"text": status}}

        response = requests.patch(
            "https://discord.com/api/v9/users/@me/settings",
            headers=headers,
            json=status_data
        )

        if response.status_code == 200:
            print(f"✅ Đã đổi trạng thái thành: {status}")
        else:
            print(f"❌ Lỗi: {response.status_code} - {response.text}")

        time.sleep(3)  # Chờ 10 giây trước khi đổi trạng thái tiếp theo
