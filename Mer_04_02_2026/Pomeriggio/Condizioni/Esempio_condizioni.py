#match - case

comando = input('inserisci comando: ')

match comando:
    case "start":
        print("Avvio")
    case "stop":
        print("Chiusura")
    case "Pausa":
        print("Stop")
    case _:
        print("comando di default come else")