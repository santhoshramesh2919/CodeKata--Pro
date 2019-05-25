#Kholi Reading book
n,t=map(int,input().split())
secs=list(map(int,input().split()))
c=0
for i in secs:
  time_remain=86400-i
  t=t-time_remain
  c+=1
  if t<=0:
    break
print(c)
