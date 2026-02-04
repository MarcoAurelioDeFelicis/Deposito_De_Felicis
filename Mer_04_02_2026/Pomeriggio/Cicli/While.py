game_over = False
counter = 0

while game_over == False:
    counter +=1 
    print(f"{counter}")
    
    scelta = input("vuoi uscire? si - no\n")
    while scelta.lower() != "si" or scelta.lower() != "no":
        scelta_2 = input("devi scegliere tra si o no")
        if scelta_2.lower() == "si":
            game_over = True
            
    if scelta.lower() == "si":
            game_over = True
