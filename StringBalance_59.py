a,b=map(str,input().split("|"))
c=input()
if len(a)>len(b):
  if len(a)==len(b+c):
    print(a+"|"+b+c)
elif len(a)<len(b):
  if len(a+c)==len(b):
    print(a+c+"|"+b)
    
elif len(a)==len(b) and len(c)>1 or (len(b)or len(a))==0:
  print("Impossible")
