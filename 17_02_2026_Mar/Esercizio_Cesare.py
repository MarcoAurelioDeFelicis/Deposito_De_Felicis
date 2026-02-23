alfabeto = "abcdefghijklmnopqrstuvwxyz"

def sposta_lettere(chiave_num, parola: str, scelta):
    # parola = parola.replace(" ", "")
    parola = parola.strip()
    nuova_parola = []
    
    if not chiave_num.isdecimal():
        print("devi inserire una parola")
        return False
    
    if scelta == "c":
    
        chiave_num = int(chiave_num)
        
        for carattere in parola.lower():
            if  carattere in alfabeto:
                indice_attuale = alfabeto.index(carattere)
                indice_new = (indice_attuale + chiave_num) %len(alfabeto)
                print(f"DEBUG: {indice_new}")
                nuova_parola.append(alfabeto[indice_new])
            else:
                nuova_parola.append(carattere)
            
        return "".join(nuova_parola)   
    
    if scelta == "d":
        
        chiave_num = int(chiave_num)
        
        for carattere in parola.lower():
            if  carattere in alfabeto:
                indice_attuale = alfabeto.index(carattere)
                indice_new = (indice_attuale - chiave_num) %len(alfabeto)
                print(f"DEBUG: {indice_new}")
                nuova_parola.append(alfabeto[indice_new])
            else:
                nuova_parola.append(carattere)
        
        return "".join(nuova_parola)
          
                
# --- PLAY ---
while True:

        scelta = input("scrivi c per criptare o d per decriptare: ").lower()
        
        if scelta not in ("c" , "d", "e"):
            print("ERRORE: scelta non valida")
            
        elif scelta == "e":
            print("CIAO!! ")
            break
            
        else:
            parola = input("scrivi la parola: ").lower() 
            if parola or not parola.isdigit():
        
                chiave_num = input("inserisci il numero della chiave: ")
                risultato = sposta_lettere(chiave_num, parola, scelta)

                if risultato:
                    print(f"risultato: {risultato}")
                
    

