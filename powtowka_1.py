wiek = int(input("Podaj wiek: "))

if wiek < 15:   #jesli mniej niz 15
    print("jesteś dzieckiem")
    print(f"do pełnoletności brakuje CI {18 - wiek} lat")
elif wiek < 18:
    print("jestes niepoełnoletni")
    print(f"do pelnoletności brakuje CI {18 - wiek} lat")
elif wiek == 18:
    print("masz dokladnie 18 lat")
elif wiek <= 60:
    print("jestes dorosly")
else:
    print("jestes stary")