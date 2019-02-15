n,p,q,r=map(int,input().split())
li=[]
a=list(map(int,input().split()))
for i in range(0,len(a)):
  for j in range(i,len(a)):
    for k in range(j,len(a)):
      li.append((p*a[i])+(q*a[j])+(r*a[k]))
print(max(li))
