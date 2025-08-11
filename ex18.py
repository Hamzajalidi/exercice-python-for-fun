age = int(input("enter l age :"))
sexe = input("enter 'h' for homme and 'f' for fomme")
if sexe =="h"and age >20:
    print("imposable")
elif sexe =="f" and 18>age <35:
    print("imposable")
else:
    print("n pas imposable")