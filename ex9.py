T = int(input("enter le nomber on secondes:"))
l=T
h = T//3600
T= T % 3600
m = T//60
s = T%60
print("=",l,"seconds =>",h,"houres",m,"minutes",s,"seconds")
