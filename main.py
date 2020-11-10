import json


def get_data(file_name):
    with open(file_name, "r") as data:
        output = json.load(data)
    return output


def constructor(file_name, given_data):
    with open(file_name, "w") as data:
        json.dump(given_data, data, indent=4, sort_keys=True)


def convert(amount, rate, data):
    for k, v in data["rates"].items():
        if k == rate:
            output = amount * v
            break
    return "{:.2f}".format(output)


def main():
    exchange_rate = get_data("exchange_rate.json")

    print("How much money would you like to convert?")

    try:
        money = float(input("=> "))
    except:
        print("That's not a valid number.\nPlease try again!")
    else:
        print("What currency would you like it in?")
        currency = input("=> ").upper()

        if currency in exchange_rate["rates"].keys():
            amount = convert(money, currency, exchange_rate)
            print(f"Converted amount is {amount} {currency}")
        else:
            print("That currency is unavailable.\nPlease try again!")


if __name__ == "__main__":
    main()