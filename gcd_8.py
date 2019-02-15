def gcd(m,n):
  li=[]
  for i in range(1,max(m,n)+2):
    if m%i==0 and n%i==0:
      li.append(i)
  return(max(li))
n,q=map(int,input().split())
li=list(map(int,input().split()))
li2=[]
for i in range(q):
  li2.append(list(map(int,input().split())))
print(li2)
