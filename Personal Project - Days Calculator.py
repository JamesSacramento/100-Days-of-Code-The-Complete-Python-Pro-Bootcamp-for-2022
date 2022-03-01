#This is a personal idea project made by me to track:
# How many days are left and to cram to other days?
# How many days elapsed?

import datetime

days_100 = 100
date_today = datetime.date.today()
start_date = datetime.date(2022, 2, 3)
days_done = int(input("How many days are done? "))

# Formulas
days_elapsed = date_today - start_date
#Time Delta integer converstion
days_elapsed_int = days_elapsed.days
#Days Left
days_left = days_100 - days_elapsed_int
#Days to be Crammed
days_crammed = days_elapsed_int - days_done

print(f"Days Elapsed: {days_elapsed_int}")
print(f"Days Left: {days_left}")
print(f"Days to be Crammed to other days: {days_crammed}")

input("Press any key to exit: ")