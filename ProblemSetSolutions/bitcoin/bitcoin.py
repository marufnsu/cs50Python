import sys
import requests

def main():
    amount = get_amount()
    print(f"${amount:,.4f}")

def get_value():
    if len(sys.argv) == 2:
        try:
            value = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")
    return value

def get_amount():
    value = get_value()
    try:
        response  = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        bitcoin = response['bpi']['USD']['rate_float']
        total_amount = bitcoin * value
    except requests.RequestException:
        sys.exit("RequestException")
    return total_amount

if __name__ == "__main__":
    main()