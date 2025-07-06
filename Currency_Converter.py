# This is a live currency converter, using API

# Start by importing the requests module
import requests

# Define the amount variable
amount = 0.0

# Ask the user to input an amount and only allow number
while True:
    try:
        amount = float(input(
            "Welcome to the currency converter, please start by inputting an amount:\n"))
        break
    except ValueError:
        print("That's not a number, please try again")


while True:
    # Ask the user which currency they want to convert from
    currency_from = input(
        "Input the currency you want to convert from:\n").upper().strip()

    # Ask the website (API) for currency data and save it in a json file
    url = f"https://open.er-api.com/v6/latest/{currency_from}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        print("Could not retrieve the data from the API, make sure you have internet access and try again")
        exit()

    # Check that the users input is a valid currency
    if "rates" in data:
        break
    else:
        print("Not a valid currency, please try again")


# Ask the user which currency they want to convert to
while True:
    currency_to = input(
        "Input the currency you want to convert to:\n").upper().strip()
    if currency_to in data["rates"]:
        break
    else:
        print("Not a valid currency, please try again")


# Define the rate variable
rate = data["rates"][currency_to]

# Define the total_amount variable
total_amount = amount * rate

# Print the amount of the selected currency and how much it equals in total
print(f"{amount} {currency_from} is {total_amount:.1f} {currency_to}")
