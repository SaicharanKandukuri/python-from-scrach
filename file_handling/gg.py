
line=str(input("menter something: "))
f = open('D:\Apps & files\Codes\python-from-scrach\/file_handling\gg.txt','w')
f.writelines(line)
f.close()
f = open('D:\Apps & files\Codes\python-from-scrach\/file_handling\gg.txt','r')
print(f.readlines())
