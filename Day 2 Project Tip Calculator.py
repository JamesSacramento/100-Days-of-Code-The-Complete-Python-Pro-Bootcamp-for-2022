greetings = print("Welcome to the tip calculator.")
bill = input("What was the total bill?\n$")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15\n")
split = input("How many people to split the bill?\n")

calculation = (float(bill) / int(split)) * (int(percentage_tip) / 100 + 1)
calculation_rounded = round(calculation, 2)
calculation_rounded = "{:.2f}".format(calculation_rounded)

result = f"Each person should pay: ${calculation_rounded}"
print(result)
