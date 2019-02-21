#Murder case
n=int(input())
li=[]
a=list(map(int,input().split()))
for i in range(0,n):
  for j in range(0,i):
    if a[i]>a[j]:
      li.append(a[j])
print(sum(li))
