n,k=map(int,input().split())
ingri=list(map(int,input().split(" ")))
grams=list(map(int,input().split(" ")))
print((sum(grams)+k)//sum(ingri))
