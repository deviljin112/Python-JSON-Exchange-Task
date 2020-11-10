import json


# Function to retrive data from a specific file
def get_data(file_name):
    with open(file_name, "r") as data:
        output = json.load(data)
    return output


def main():
    # Pulls all the exchange rates into a dictionary
    exchange_rate = get_data("exchange_rate.json")

    print("What would you like to access?\n'all data' or 'country' codes.")
    choice = input("=> ")

    if choice.lower() == "country":
        for k in exchange_rate["rates"].keys():
            print(k)
    elif choice.lower() == "all data":
        for k, v in exchange_rate["rates"].items():
            print(f"{k}: {v}")
    else:
        print("That option is unavailable.\nPlease try again!")


if __name__ == "__main__":
    main()