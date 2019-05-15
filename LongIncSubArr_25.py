n=int(input())
li=list(map(int,input().split()))
l=1
m=1
op=[]
for i in range(1,len(li)):
  if li[i]>li[i-1]:
    l=l+1
  else:
    l=1
  op.append(l)
print(max(op))
