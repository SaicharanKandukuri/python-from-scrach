# Tuple -> odered and unchangeable

student=("Saicharan",18,"male")
print(student.count(18))

print(student.index(18))

for i in student:
    print(i)
    
if "Saicharan" in student:
    print(":)")
else:
    print(":(")