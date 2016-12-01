from turtle import*
speed(-1)
x=4
for i in range(6):
       for a in range(x):
              m=a%2
              if m==1:
                     color('red')
                     lt(360/x)
                     fd(100)
              elif m==0:
                     color('blue')
                     lt(360/x)
                     fd(100)
       
       x+=1
