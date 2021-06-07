# The Box maker with boundary
rows=int(input("How Many rows : "))
columns=int(input("How many columns : "))
symbols = input("Symbols or charceter : ")
times=columns+4
print("-"*times)

for i in range(rows):
    print("| ", end="")
    for j in range(columns):
        print(symbols, end="")
    print(" |", end="")
    print()

print("-"*times)