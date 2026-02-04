def max_numero(numeri: list):
    max_num = numeri[0]
    for n in numeri:
        if n >= max_num:
            max_num = n
            
    return print(f"numero massimo di {numeri} è '{max_num}' \n")


def len_numeri(numeri: list):
    game_over = False
    count = 0
    counted_num = []
    while not game_over:
        for n in numeri:
            if not n in counted_num:
                counted_num.append(n)
                count += 1
            else:
                game_over = True
            
    return print(f"la lista di numeri che mi hai dato contiene {count} numeri")
    
def check_lista(numeri: list):
    if len(numeri) > 0:
        max_numero(numeri)
        len_numeri(numeri)
    else:
        print("Lista Vuota")
        
    
def execute_es4(numeri: list):
    check_lista(numeri)
    
