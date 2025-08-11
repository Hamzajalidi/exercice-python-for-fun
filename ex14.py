x = int(input("enter le nomver de photocopies:"))
if x<=10:
    a=x*0.30
elif 10<x<=30:
    a=(x-10)*0.25+10*0.30
elif x>30:
    a=(x-30)*0.20+0.25*20+0.30*10
print("la facteur de correspondante est:",a)
