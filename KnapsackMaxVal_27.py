n,W=map(int,input().split())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
ratio=[v[i]/w[i] for i in range(n)]
count=0
while W>=0 and len(ratio)>0:
  ind=ratio.index(max(ratio))
  if W>=w[ind]:
    count+=v[ind]
    W=W-w[ind]
  w.pop(ind)
  v.pop(ind)
  ratio.pop(ind)
print(count)
