
line=str(input("menter something: "))
f = open('gg.txt','w')
f.writelines(line)
f.close()
f = open('gg.txt','r')
print(f.readlines())
