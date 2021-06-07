# for Loop -> statement that executes its code a limited amount of time
import time

seconds=int(input("Enter no.of seconds to countdown .. "))

for i in range(seconds,0,-1):
    print(i)
    time.sleep(1)
print("\aYour "+str(seconds)+" timer is done!...")
