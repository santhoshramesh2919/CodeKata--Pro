n=int(input())
t=sorted(list(map(int,input().split())))
sats=1
for i in range(1,n):
  if sum(t[:i])<=t[i]:
    sats+=1
print(sats)
