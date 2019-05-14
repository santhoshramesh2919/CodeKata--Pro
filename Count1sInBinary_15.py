def bitCount(n):
  count=0
  while n!=0:
    if n%2==1:
      count+=1
    n=n//2
  return count

n=int(input())
li=list(map(int,input().split(" ")))
dic={}
for i in li:
  dic[i]=bitCount(i)
dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
for i in dic:
  print(i[0])
  
