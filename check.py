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
        "Content-Type": "application/json"
    }

    response = requests.post(URL, json=payload, headers=headers)
    return response.json()

for date in TARGET_DATES:
    result = check_date(date)
    print(date, result)
