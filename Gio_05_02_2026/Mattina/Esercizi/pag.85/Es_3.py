
while True:
    val1 = input("Inserisci il primo valore: ")
    val2 = input("Inserisci il secondo valore: ")

    if val1.isdigit() and val2.isdigit():
        num1 = int(val1)
        num2 = int(val2)

        fattori_comuni = []
        limite = min(num1, num2)

        for i in range(1, limite + 1):
            if num1 % i == 0 and num2 % i == 0:
                fattori_comuni.append(i)

        print(f"\nFattori comuni: {fattori_comuni}")
        
        if len(fattori_comuni) == 1 and fattori_comuni[0] == 1:
            print("I numeri sono coprimi")
        
    else:
        s1 = val1.lower()
        s2 = val2.lower()

        set1 = set(s1)
        set2 = set(s2)

        if set1 == set2:
            print("\nLe stringhe sono complementari")
        else:
            print("\nLe stringhe NON sono complementari")

    while True:
        ripeti = input("\nVuoi ripetere l'operazione? (y/n): ").lower()
        if ripeti in ("y", "n"):
            break
        print("Scelta non valida, inserisci y o n.")

    if ripeti == "n":
        print("Ciao!")
        break
    else:
        print("\n--- Nuova esecuzione ---\n")
