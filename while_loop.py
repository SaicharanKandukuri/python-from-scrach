name = None
x=0

while not name:
    x=x+1
    if x<3:
        name = input("Enter your name: ")
    if x==3:
        name = input("Man enter your name : ")
    if x==4:
        name = input("Why are spamming mate: ")
    if x==5:
        name = input("For God sake: ")
    if x==6:
        name = input("Bro!........")
    if x==7:
        print("Iam out mate!")
        exit(0)       
    
print("Hello "+ name)
if x>=5:
    print("Nice to hear you name :)")