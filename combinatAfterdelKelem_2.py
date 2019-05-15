from itertools import combinations
n,k=map(str,input().split())
l=list(combinations(n,len(n)-int(k)))
l=sorted(l)
print("".join(l[0]))
