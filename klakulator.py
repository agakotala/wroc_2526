print("kalkulator prosty")
print("możesz robić nastepujące operacje: +, -, *, /")

a = float(input("Podaj pierwsza liczbe: "))
oper = input("podaj co chcesz zrobic (+, -, *, /): ")
b = float(input("podaj druga liczbe: "))

if oper == "+":
    wynik = a + b
elif oper == "-":
    wynik = a -b
elif oper == "*":
    wynik = a * b
elif oper == "/":
    if b != 0:
        wynik = a / b
    else:
        print("nie mozna dzielic przez 0")
        exit()
else:
    print("niepoprawna operacja")
    exit()
if wynik is not None:
    print(f"wynik: {a} {oper} {b} = {wynik}")

