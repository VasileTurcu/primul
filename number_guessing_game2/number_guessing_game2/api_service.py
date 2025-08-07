import requests

class ApiService:
    def __init__(self):
        self.api_url = "https://httpbin.org/post"  # API de test

    def send_score(self, name, wins, losses):
        data = {
            "name": name,
            "wins": wins,
            "losses": losses
        }
        try:
            response = requests.post(self.api_url, json=data)
            if response.status_code == 200:
                print("📡 Scorul a fost trimis cu succes către API.")
            else:
                print("⚠️ Eroare la trimiterea datelor către API.")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Nu s-a putut realiza conexiunea la API: {e}")