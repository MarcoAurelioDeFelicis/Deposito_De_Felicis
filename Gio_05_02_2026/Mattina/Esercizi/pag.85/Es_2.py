while True:
    try:
        inizio = int(input("Inserisci il primo numero: "))
        fine = int(input("Inserisci il secondo numero: "))
    except ValueError:
        print("Devi inserire numeri interi!")
        continue

    numeri_primi = []
    numeri_non_primi = []

    #direzione del ciclo
    if inizio <= fine:
        step = 1
    else:
        step = -1

    for numero in range(inizio, fine + step, step):
        if numero < 2:
            numeri_non_primi.append(numero)
        else:
            primo = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    primo = False
                    break

            if primo:
                numeri_primi.append(numero)
            else:
                numeri_non_primi.append(numero)

    print(f"\nNumeri primi: {numeri_primi}")
    print(f"Numeri non primi: {numeri_non_primi}")

    while True:
        ripeti = input("\nVuoi ripetere il programma? (y/n): ").lower()
        if ripeti in ("y", "n"):
            break
        print("Scelta non valida, inserisci y o n.")

    if ripeti == "n":
        print("Ciao!")
        break
    else:
        print("Ok, ripartiamo!\n")
