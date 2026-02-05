game_over = False
stop = False
numero = 0
parola = ""
valore= "Null"
scelte_disponibili = ["stampare", "ripetere", "stop"]

while not game_over:
    stop = False
    user = input("iserisci un numero oppure una stringa ")
    while not stop:
        try:
            numero = int(user)
            user = numero
        except:
            parola = user
            user = parola
            
        if isinstance(user, str):
            count = 0
            for l in user:
                count +=1
            if count % 2 == 0:
                valore = "pari"
            else:
                valore = "dispari"
        elif isinstance(user, int):
            if user % 2 == 0:
                valore = "pari"
            else:
                valore = "dispari"
                
        print(f"Il tuo valore è {valore}")
        
        scelta = input("cosa vuoi fare ora stampare - ripetere - stop?")
        if scelta == "" or scelta not in scelte_disponibili:
            print("devi scegliere tra stampare - ripetere - stop")
        else:
            match scelta.lower():
                case "stampare":
                    print(f"il tuo valore è {valore}")
                    
                case "ripetere":
                    print("continuiamo")
                    stop = True
                    pass
                    
                case "stop":
                    print("Ciao!")
                    stop = True
                    game_over = True
            
        