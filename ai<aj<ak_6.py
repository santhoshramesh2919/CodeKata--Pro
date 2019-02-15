n=int(input())
count=0
a=list(map(int,input().split()))
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    for k in range(j+1,len(a)):
      if a[i]<a[j] and a[j]<a[k]:
        print(a[i],a[j],a[k])
        count+=1
        break
print(count)
