import sys
import requests
import json
try:
    n=float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=42b77730c73542fb9abf1bb81d062d2d9c83fbf25cc814844a44792a5f530524")
    #print(json.dumps(response.json(), indent=2))

    o = response.json()
    amount=float(o["data"]["priceUsd"]) * n
    print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    print("error")
except IndexError:
    sys.exit("Missig command-line argument")


