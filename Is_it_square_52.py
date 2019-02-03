import math
x1,y1=map(int,input().split(" "))
x2,y2=map(int,input().split(" "))
x3,y3=map(int,input().split(" "))
x4,y4=map(int,input().split(" "))
dif1=((x2-x1)**2)+((y2-y1)**2)
d1=math.sqrt(dif1)
dif2=((x3-x2)**2)+((y3-y2)**2)
d2=math.sqrt(dif2)
dif3=((x4-x3)**2)+((y4-y3)**2)
d3=math.sqrt(dif3)
dif4=((x1-x4)**2)+((y1-y4)**2)
d4=math.sqrt(dif4)
if d1==d2 and d2==d3 and d4==d3 and d1==d4:
    print("yes")
else:
    print("no")
