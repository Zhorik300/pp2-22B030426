import re
p=str(input())
x=re.findall("ab{2,3}",p)
print(x)
if x:
    print("Yes")
else:
    print("No")
