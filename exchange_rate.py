import json


# Function to retrive data from a specific file
def get_data(file_name):
    with open(file_name, "r") as data:
        output = json.load(data)
    return output


# Function to convert amount to specified rate
def convert(amount, rate, data):
    for k, v in data["rates"].items():
        if k == rate:
            output = amount * v
            break
    return "{:.2f}".format(output)


def main():
    # Pulls all the exchange rates into a dictionary
    exchange_rate = get_data("exchange_rate.json")

    print("How much money would you like to convert?")

    # Tries to convert the input into a float
    try:
        money = float(input("=> "))
    except:
        print("That's not a valid number.\nPlease try again!")
    else:
        # If successful then continues with the code
        print("What currency would you like it in?")
        currency = input("=> ").upper()

        # Checks that specified currency exists
        if currency in exchange_rate["rates"].keys():
            # Triggers the function and return data is assigned return value to a variable
            amount = convert(money, currency, exchange_rate)
            print(f"Converted amount is {amount} {currency}")
        else:
            print("That currency is unavailable.\nPlease try again!")


if __name__ == "__main__":
    main()