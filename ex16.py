N1 = float(input("enter la note :"))
N2 = float(input("enter la note :"))
N3 = float(input("enter la note :"))
M=(N1+N2+N3)/3
if M >= 16:
    print("tres bien")
elif M>=14 and M<16:
    print("Bien")
elif M>=12 and M <14:
    print("assez bien")
elif M>=10 and M<12:
    print("Passable")
elif M<10:
    print("Insuffisant")
    