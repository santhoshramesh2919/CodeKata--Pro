str1=input().lower()
li=[]
for i in str1:
    if i==" ":
        continue
    else:
        li.append(i)
se=set(li)
if len(se)==26:
    print("yes")
else:
    print("no")
