n,k=map(int,input().split())
flag=0
li=list(map(int,input().split()))
for i in range(len(li)-1):
  for j in range(i+1,len(li)):
    if li[i]+li[j]==k:
      flag=1
      print("yes")
      break
  if flag==1:
    break
else:
  print("no")
