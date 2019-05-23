#Lexicographcal
s=input()
for i in range(len(s)):
  substr=s[i::]
  if substr[0]>s[0]:
    print(substr)
    break
