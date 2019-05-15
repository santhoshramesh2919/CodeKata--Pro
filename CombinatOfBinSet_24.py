#Binary Set Definitions
from itertools import product
n=int(input())
li=list(map(list,product([0,1],repeat=n)))
for i in li:
    for j in range(n):
        if j==n-1:
            print(i[j])
        else:
            print(i[j],end="")
        
