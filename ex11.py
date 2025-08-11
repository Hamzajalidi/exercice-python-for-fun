R1 = float(input("enter la valeur de R1 :"))
R2 = float(input("enter la valeur de R2 :"))
R3 = float(input("enter la valeur de R3 :"))
Rser =R1+R2+R3
Rpar=(R1*R2*R3)/(R1*R2+R1*R3+R2*R3)
print("la valeur de la résistance en série est :",format(Rser,".2f"))
print("la valeur de la résistance en paraé5lle est :",format(Rpar,".2f"))