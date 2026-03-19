import sys
import requests


def main():
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&precision=4"

    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    try:
        quantity = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(api_url)
        data = response.json()
        btc_price = data["bitcoin"]["usd"]
    except requests.RequestException:
        sys.exit("Error fetching")

    print(f"${(btc_price * quantity):,.04f}")


if __name__ == "__main__":
    main()
