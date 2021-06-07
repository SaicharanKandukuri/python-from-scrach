# Logical Operators
temp = int(input("What is temperature ? :"))
if temp>= 0 and temp <=30:
    print("Temperature is good today ! ")
    print(" You can go outside at " + str(temp))
elif  temp < 0:
    print(" Its really bad Get some fire ! ...")
elif  temp > 100:
    print("You are not in planet earth or earth is going to die !..")
    print("Get Out of the planet :)..")
    while True:
        print("Earth is going to die")
