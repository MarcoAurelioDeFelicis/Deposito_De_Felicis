# reate un programma che richiede all’utente tre numeri 
# e verifica la presenza di almeno due numeri uguali, 
# se non ci sono ci restituisce il numero più grande dei tre

def inserisci_numero(etichetta):
    while True:
        valore = input(f"Inserisci numero {etichetta}: ")
        if valore.replace('-', '', 1).isdigit(): 
            return int(valore)
        print("Errore: Devi inserire un numero intero. Riprova.")

num_A = inserisci_numero("A")
num_B = inserisci_numero("B")
num_C = inserisci_numero("C")

lista_numeri = [num_A, num_B, num_C]
# lista_numeri.pop()
print(lista_numeri)

if num_A == num_B or num_A == num_C or num_B == num_C:
    print(f"\nRisultato: Almeno due numeri sono uguali! {lista_numeri}")
else:
    maggiore = 0
    for num in lista_numeri:
        if num >= maggiore:
            maggiore = num
    print(f"\nNessun duplicato trovato. Il numero più grande è: {maggiore}")