import random
import sys

def genera_numero():
    random_int = random.randint(1, sys.maxsize)
    print("rand_int = ", random_int)
    return random_int

def casuale_senza_limiti():
    n = 1
    while random.random() < 0.5:
        n += 1
    print("rand_infinito = ", n)
    return n

def fibonacci(n: int):
    a, b = 0, 1
    while a <= n:
        yield a  # "Sospende" la funzione e restituisce il valore
        a, b = b, a + b
        
def catena_generazione():
    pass
    
    
for valore in fibonacci(genera_numero()):
    print(valore)