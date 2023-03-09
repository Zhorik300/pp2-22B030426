
import re
x=str(input())
p=re.findall("a(b*)$", x)
if p:
    print("Yes")
else :
    print ("No")

