a=input("radius?")
print("area=",int(a)*31.4)
c=input("enter the temperature in celsius?")
print(c,"(c) =",int(c)*1.8+32,"(f)")
m=input("how many b bacterias are there?")
n=input("how much time will we wait?")
print("after",n,"minutes we would have",int(m)*pow(2,int(n)//2),"bacterias")
x=int(input("month?"))
z=1
y=1
for i in range(x):
    o=z+y
    if i==0 or i==1:o=1
    print("month",i,":",int(o),"pair(s) of rabbits")
    y=z
    z=o
