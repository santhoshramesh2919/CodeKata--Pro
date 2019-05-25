n=input()
i=len(n)-1
c=0
while(1):
  if n[i]=="0":
    c+=1
    i-=1
  else:
    break
if n==n[::-1]:
  print("yes")
else:
  n="0"*c+n
  if n==n[::-1]:
    print("yes")
  else:
    print("no")
