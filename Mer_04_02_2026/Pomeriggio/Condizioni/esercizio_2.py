operatori = ['+', '-', '*', '/']
num_a = int(input("inserisci il numero 'a': "))
operatore = (input("inserisci un operatore tra( + - + /)"))
if operatore not in operatori :
    print("Errore: operatore non valido!")
    exit()
num_b = int(input("inserisci il numero 'b': "))

risultato = 0

if isinstance(num_a, int) and isinstance(num_b, int):
    match operatore:
        case "+":
            risultato = num_a + num_b
            print(f"il risultato dell'addizione {num_a} + {num_b} = {risultato}\n")
        case "-":
            risultato = num_a - num_b
            print(f"il risultato dell'sottrazione {num_a} - {num_b} = {risultato}\n")
        case "*":
            risultato = num_a * num_b
            print(f"il risultato dell'moltiplicazione {num_a} * {num_b} = {risultato}\n")
        case "/":
            if num_a == 0 or num_b == 0:
                print("errore divisione per 0")
            else:
                risultato = num_a / num_b
                print(f"il risultato dell'addizione {num_a} + {num_b} = {risultato}")
        case _:
            print("mi Dispiace segui le regole \n\n\n")
            exit()
else:
    print("devi inserire numeri \n\n\n")
            