import requests

URL = "https://hnd-rsv.aeif.or.jp/airport2/app/calendar"

TARGET_DATES = [
    "2026/03/14",
    "2026/03/15",
    "2026/03/16",
    "2026/03/17"
]

def check_date(date):
    payload = {
        "date": date,
        "area": "0",
        "handicapped": "0"
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://hnd-rsv.aeif.or.jp/airport2/app/member/yoyaku/nyuryoku_kakunin"
    }

    response = requests.post(URL, json=payload, headers=headers)

    print("Status:", response.status_code)
    print("Raw response:", response.text[:500])  # デバッグ用

    return response.text


for date in TARGET_DATES:
    result = check_date(date)
    print("-----", date, "-----")
