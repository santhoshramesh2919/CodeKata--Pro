n=int(input())
li=list(map(int,input().split()))
extr=0
for i in range(1,len(li)-1):
  if (li[i]<li[i-1] and li[i]<li[i+1]) or (li[i]>li[i-1] and li[i]>li[i+1]):
    extr+=1
print(extr)
