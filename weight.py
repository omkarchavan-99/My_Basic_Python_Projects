weight=float(input("Weight: "))
unit=input("The Input Weight Is In (l)lbs or (kg)kg: ")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"you are {converted:.2f} kilos")
else:
    converted=weight/0.45
    print(f"you are {converted:.2f} lbs")