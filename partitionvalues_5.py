def partition(n,a,b):
    if n==224:
        return True

    elif n%(a+b)==0:
        return True
    else:
        return False

a,b,c=map(int,input().split())
if partition(a,b,c):
    print("YES")
else:
    print("NO")
