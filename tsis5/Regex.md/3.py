import re 
p=str(input())
x=re.findall("\w",p)
print(x)
if x:
    print("Yes")
else:
    print("No")
