import re 
p=str(input())
x=re.findall("[A-Z]+[a-z]+$",p)
print(x)
if x:
    print("Yes")
else:
    print("No")
