n=int(input())
li=list(map(int,input().split()))
extr=0
for i in range(len(li)):
  if li[0]==li[len(li)-1]:
    break
  if i==0 or i==len(li)-1:
    extr+=1
  elif (li[i]<li[i-1] and li[i]<li[i+1]) or (li[i]>li[i-1] and li[i]>li[i+1]):
    extr+=1
print(extr)
