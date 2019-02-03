str1=list(input())
str2=list(input())
str3=""
li1,li2=[],[]
for i in str1:
    li1.append(ord(i)%96)
for i in str2:
    li2.append((ord(i))%96)
for z in range(0,len(li1)):
    s=li1[z]+li2[z]
    t=s+96
    if t>122:
        t=t-26
        str3+=chr(t)
    else:
        str3+=chr(t)

print(str3) 
