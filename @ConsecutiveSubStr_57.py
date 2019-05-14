a,b=map(str,input().split(" "))
for i in range(len(a)-2):
  if a[i:i+2] in b:
    print("yes")
    break;
else:
  print("no")
  
