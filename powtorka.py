#instrukcja warunkowa
imię = input("Jak masz na imię? ") #zapyta o imię
if imię == "Ola":     #warunek 1
    print("cześć Ola, miło Cię widzieć!") #zwróć
elif imię == "Antek":           #warunek 2
    print("Witaj Antek! co słychać?") #zwróc
else:
    print(f"Hejka {imię}!") #jak nie zostaną spełnione powyższe zwróc hejka