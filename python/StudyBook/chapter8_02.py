file = open("text.dat",'r')
file1 = open("text.dat",'w')

print(dir(file))
print(dir(file1))

file1.write("wenhui hello ");
file1.flush()

input()
