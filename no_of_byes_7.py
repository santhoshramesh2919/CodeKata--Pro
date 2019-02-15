#no_of_byes
n=int(input())
li=[]
i=1
while((2**i)<=n):
  li.append(2**i)
  i+=1
print(n-max(li))
