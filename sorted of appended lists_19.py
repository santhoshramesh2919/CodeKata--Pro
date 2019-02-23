# Soted of appended lists
n=int(input())
li=[]
for i in range(n):
  li+=(list(map(int,input().split())))
print(*sorted(li))
