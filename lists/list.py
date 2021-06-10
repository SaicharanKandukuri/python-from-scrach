# list = multiple values in one

marvel = ["iron man", "Hulk", "Natash Romnaf", "Bruce Banaer", "thor", "HAwkeye", "War machine"]
marvel[0] = "Tony stark"
print(marvel[1])
print(marvel[0])


marvel.append("vision")
marvel.append("wanda")

marvel.sort()

for x in marvel:
    print(x)