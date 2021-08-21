import re

r1=re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$')
a=input("enter the variable")
b=r1.fullmatch(a)

if (b!=None):
    print("valid")
else:
    print("invalid")