n=int(input())

li=list(map(int,input().split()))
op=[]
for j in range(len(li)):
  c=1
  for i in range(j,len(li)-1):
    if (li[i]>0 and li[i+1]<0) or (li[i]<0 and li[i+1]>0):
      c+=1
    else:
      break
  op.append(c)

print(*op)
