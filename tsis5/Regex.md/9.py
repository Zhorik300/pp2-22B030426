import re
p=input()
x=re.sub(r"(\w)([A-Z])", r"\1 \2", p)
print (x)
if x:
    print('Yes')
    
else :
    print("No")
