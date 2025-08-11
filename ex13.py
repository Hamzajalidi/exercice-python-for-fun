a = int(input("enter la valeur de a :"))
b = int(input("enter la valeur de b :"))
if a * b > 0:
    a, b = b, a
else:
    c = a
    a = a+b
    b = c*b
print("a= ", a, "b=", b)
