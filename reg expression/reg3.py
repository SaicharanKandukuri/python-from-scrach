import re

r1=re.compile('[_a-zA-Z][_a-zA-Z0-9]*')
a=input("enter the variable")
b=r1.fullmatch(a)

if (b!=None):
    print("valid")
else:
    print("invalid")