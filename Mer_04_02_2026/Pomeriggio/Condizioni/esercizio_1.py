eta= int(input("Quanti anni Hai?"))
eta_check = ""

if int(eta) >= 18 :
    eta_check = "maggiorenne"
else:
    eta_check = "minorenne"
 

match eta_check:
    case "maggiorenne":
        print("Puoi Vedere Questo Film")
    case _:
        print("mi Dispiace non pui Vedere il Film")