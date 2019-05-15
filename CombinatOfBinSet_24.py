#Binary Set Definitions
from itertools import product
n=int(input())
li=list(map(list,product([0,1],repeat=n)))
for i in li:
    print(*i)

