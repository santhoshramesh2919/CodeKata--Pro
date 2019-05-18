n=int(input())
quan=list(map(int,input().split()))
a=0
b=0
quan.sort(reverse=True)
for i in quan:
  equa=a+i
  if b>equa:
    a=equa
  else:
    a=b
    b=equa
print(a,b)
