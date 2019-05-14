n,t=map(int,input().split(" "))
li=list(map(int,input().split()))
c=0
li.sort(reverse=True)
if t%max(li)==0:
  print(t//max(li))
else:
  i=0
  while t!=0:
    c=c+(t//li[i])
    t=t%li[i]
    li.pop(i)
  print(int(c))
