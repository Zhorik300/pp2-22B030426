import re 
p=str(input())
x=re.findall("a.*b$",p)
print(x)
if x:
    print("Yes")
else:
    print("No")
