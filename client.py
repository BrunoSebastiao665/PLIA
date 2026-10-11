import requests

def main():
    url = "http://localhost:5000/predict"
    sample = {"instances": [[5.1, 3.5, 1.4, 0.2]]}
    r = requests.post(url, json=sample)
    print("Status:", r.status_code)
    try:
        print(r.json())
    except Exception:
        print(r.text)

if __name__ == "__main__":
    main()
