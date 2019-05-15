n=int(input())
li=list(map(int,input().split()))
for i in range(1,len(li)):
    if (sum(li[:i]))//len(li[:i])==(sum(li[i:]))//len(li[i:]):
        e=1
        break
    else:
        e=0
if e==1:
    print("yes")
else:
    print("no")
    
