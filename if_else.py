# if else 
#       A
#       |
#   |--------|
#  |          |
# True     False
#  |          |
# do_this    do_this

gg=input("Enter You name : ")
if gg.isdigit() != 0:
    print("Name should be a charecter bro !")
gg=input("Enter You name : ")
if gg.isdigit() != 0:
    print("You are out you mind bro !")
    exit(0)
else:
    print("O! hello"+gg)
    