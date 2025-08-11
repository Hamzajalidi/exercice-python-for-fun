pht = float(input("enter la valeur de pht:"))
c = input("enter la categorie 'a' or 'b' or 'c':")
if c =="a":
    pttc = pht + pht *0.07
if c =="b":
    pttc = pht + pht *0.2
if c =="c":
    pttc = pht + pht *0.25
print("pttc = ",pttc)