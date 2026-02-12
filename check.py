import requests

url = "https://parking.haneda-airport.jp/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Length:", len(response.text))
