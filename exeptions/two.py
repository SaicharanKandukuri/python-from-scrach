import sys
lst = [2,0,'A',"str",3.4,-98]

for i,j in zip(lst,range(1,10)):
    print(j,"--------")
    try:
        print(1/int(i))
    except Exception as error:
        print(sys.exc_info()[0])
        print(error)