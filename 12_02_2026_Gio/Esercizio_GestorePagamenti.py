# creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. 
# Questo scenario permetterà di vedere il polimorfismo in azione, 
# permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, 
# pur aderendo all'interfaccia comune definita dalla classe base.

# Classe MetodoPagamento:
# Metodi:
# effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
# Classi Derivate:
# CartaDiCredito:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
# PayPal:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
# BonificoBancario:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
# GestorePagamenti:
# Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, 
# senza preoccuparsi del dettaglio del metodo di pagamento.

class MetodoPagamento:
    def __init__(self):
        pass
        # self.metodi_disponibili = ['paypall', 'bonifico']
    
    def effettua_pagamento(self, importo: float):
        pass
        
        
class CartaDiCredito(MetodoPagamento):
    def __init__(self, titolare):
        self.titolare = titolare

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ approvato per {self.titolare} via Carta di Credito.")
        
        
class PayPal(MetodoPagamento):
    def __init__(self, email):
        self.email = email

    def effettua_pagamento(self, importo):
        print(f"Link di pagamento inviato a {self.email}. Importo: {importo}€.")
    
        
class BonificoBancario(MetodoPagamento):
    def __init__(self, iban):
        self.iban = iban

    def effettua_pagamento(self, importo):
        print(f"Ricezione ordine per {importo}€. accredito su {self.iban}.")
             
        
class GestorePagamenti:
    def __init__(self, metodo_scelto):
        self.metodo_scelto = metodo_scelto

    def esegui_transazione(self, cifra):
        self.metodo_scelto.effettua_pagamento(cifra) 




# --- Test ---
def play():
    print("--- Benvenuto nel Checkout Dinamico ---")
    
    try:
        importo = float(input("Inserisci l'importo da pagare: "))
    except ValueError:
        print("Errore: Inserisci un numero valido.")
        return

    print("\nScegli il metodo di pagamento:")
    print("1. Carta di Credito")
    print("2. PayPal")
    print("3. Bonifico Bancario")
    
    scelta = input("Inserisci il numero della tua scelta: ")

    if scelta == "1":
        nome = input("Intestatario carta: ")
        metodo = CartaDiCredito(nome)
    elif scelta == "2":
        email = input("Email PayPal: ")
        metodo = PayPal(email)
    elif scelta == "3":
        iban = input("Inserisci il tuo IBAN: ")
        metodo = BonificoBancario(iban)
    else:
        print("Scelta non valida.")
        return

    carrello = GestorePagamenti(metodo)
    carrello.esegui_transazione(importo)

if __name__ == "__main__":
    while True:
        play()
        ancora = input("Vuoi fare un altro acquisto? (s/n): ").lower()
        if ancora != 's':
            print("Grazie e arrivederci!")
            break