n=int(input())
li=[]
for i in range(n):
  li.append(input())
minlen=len(min(li,key=len))
for i in range(len(li)-1):
  for j in range(minlen):
    if li[i][:j+1] in li[i+1]:
      t=li[i][:j+1]
print(t)

