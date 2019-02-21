def xor(li,m,n):
  s=0
  for i in range(m,n+1):
    s^=li[i]
  return(s)

n,q=map(int,input().split())
li=list(map(int,input().split()))
li2=[]
for i in range(q):
  li2.append(list(map(int,input().split())))
for i in range(len(li2)):
  print(xor(li,li2[i][0]-1,li2[i][1]-1))
