# Python-JSON-Exchange-Task

## Requirements

You will need to import the following modules into your project:

- `import json`

## JSON

Our exchange data is stored in a JSON file. We therefore will need a `get_data` function that will be used to retrive the JSON data and store it in a python dictionary. For that we will be using `open()` function.

```python
def get_data(file_name):
    with open(file_name, "r") as data:
        output = json.load(data)
    return output
```

## Input

Our dictionary converts from EURO into other currencies. We can ask the user to input how much money they would like to convert and into what currency. Because money is stored in a float, we need to use the `Try: Except:` to convert the input into a float and handle any errors in case the user inputs a different data type.

```python
try:
    money = float(input("=> "))
except:
    print("That's not a valid number.\nPlease try again!")
else:
    # If successful then continues with the code
```

## Conversion

We need to access the dictionary with conversion rates, and multiply our given amount by the conversion rate in the dictionary. To do that we can use a for loop that iterates over the key-value pairs of the rates dictionary. We only want to look at the value of the rate that matches the one that user wanted and multiply that with the amount of money the user would like to convert. We also want to format our returned value to 2 decimal places as there is no £0.001 available.

```python
def convert(amount, rate, data):
    for k, v in data["rates"].items():
        if k == rate:
            output = amount * v
            break
    return "{:.2f}".format(output)
```
