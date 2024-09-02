import os
os.system("cls")

"""

DATATYPER I PYTHON
sträng, string = "text"
heltal, integer = 1... 2... 3... 10
flyttal, float = 1.2    skriv alltid flyttal med punkt som
                        decimal
boolesk, boolean = True/False    flagga eller av och på


deklarera / intitiera 

let value; #deklarera

"""

#intitiera (namn på variabel samt datatyp)
name = " "  #string
value = 1.3 #float
value2 = 8  #integer
value3 = 8.1    #float
check = False   #boolean




x = int(input("x: "))       #input är sträng från början - du måste typkonvertera innan du gör beräkningar.
y = int(input("y: "))


print(x+y)
print(x-y)
print(x*y)
print(x**y) # upphöjt görs med ** likt som när man skriver 5^2 i miniräknare.
print(x/y, x//y) # Division
print("svar;", x % y) # Hur mycket finns kvar efter.




name = input("Vad heter du smnygging? ")
age = int(input("Hur gammal är du gubben"))
weeks = age * 52
print("Välkommen " + name + " you have lived ", str(weeks), " veckor(=")



Height = float(input("Höjd: "))
Weight = float(input("Vikt: "))

print(Weight/Height**2)


kilogram = float(input("How many kilograms?: "))
print(kilogram*2.205, "lbs")