n=int(input())
li=list(map(int,input().split()))
op=[]
c=1
for i in li:
  if i not in op:
    op.append(i)
for i in range(len(op)-1):
  if op[i]<op[i+1]:
    c+=1
print(c)
