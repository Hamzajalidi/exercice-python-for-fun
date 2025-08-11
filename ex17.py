import math
a = float(input("enter la valeur de a :"))
b = float(input("enter la valeur de b :"))
c = float(input("enter la valeur de c :"))
dilta = b ** 2 - 4 * a * c
if dilta < 0:
    print("n pas un solution ")
elif dilta == 0:
    s = -1*b/2*a
    print(s)
elif dilta > 0:
    s1 = (-1*b-math.sqrt(dilta))/(2*a)
    s2 = (-1*b+math.sqrt(dilta))/(2*a)
    print("s1 =", s1, "s2=", s2)
