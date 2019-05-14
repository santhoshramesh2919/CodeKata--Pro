x,y=map(str,input().split(" "))
li=[]
for j in range(1,len(x)):
  if x[0:j+1] in y:
    li.append(x[0:j+1])
if li==[]:
  print(len(y))
else:
  l=len(max(li))
  print(len(y)-l)
