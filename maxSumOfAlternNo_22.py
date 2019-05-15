n=int(input())
li=list(map(int,input().split()))
op=[]
for j in range(2,len(li)-1):
    for i in range(len(li)):
        l=(li[i::j])
        op.append(sum(l))
print(max(op))    
    
