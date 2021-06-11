# set -> unordered, unindexed, nuduplicate
# changable

utensils = {"gg", "ff", "ll"}
ll={"jj","kk", "oo"}
utensils.add("ii")
utensils.update(ll)

gg=utensils.union(ll)
for i in gg:
    print(i)
    
print(utensils.difference(ll))
print("-"*8)
print(utensils.intersection(ll))