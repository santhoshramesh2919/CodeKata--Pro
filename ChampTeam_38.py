n,k=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
team=0
i=0
flag=0
while i<len(li)-2:
  a,b,c=li[i:i+3]
  for j in range(k):
    a,b,c=a+1,b+1,c+1 
    if a<=5 and b<=5 and c<=5:
      flag=1
    else:
      flag=0
  if flag==1:
    team+=1
  i+=3
  a,b,c=0,0,0
print(team)
