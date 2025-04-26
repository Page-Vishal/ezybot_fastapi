import requests

url = "http://localhost:8000/chat"

querys = ["Find me 2 bedroom room in kathmandu"]

for query in querys:
    payload = {"query" : query}
    response = requests.post(url, json=payload)

    print(f"\nQuery: {query}")
    print("Status Code:", response.status_code)

    try:
        data = response.json()
        print("Response:", data["response"])
    except Exception as e:
        print("Error decoding response:", e)
        print("Raw text:", response.text)