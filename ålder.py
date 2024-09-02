
import os

os.system("cls")

from datetime import date

date_of_birth = int(input("Jag heter Tristan, året jag var född är:- "))

today_date = date.today().strftime("%Y")

print("Min ålder är: ", int(today_date)-date_of_birth, "\n\n")


