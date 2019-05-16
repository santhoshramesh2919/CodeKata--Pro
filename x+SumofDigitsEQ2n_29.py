n=int(input())
li=[]
for i in range(n):
  s=0
  temp=i
  while(temp!=0):
    s+=(temp%10)
    temp=temp//10
  if i+s==n:
    li.append(i)
print(len(li))
for i in li:
  print(i)
