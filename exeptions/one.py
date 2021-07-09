try:
    file = open("te.txt","r")
    file.read()

except ZeroDivisionError:
    print("no such file in this dir")

else:
    file.close()
    print("file closed")