##count = 0
##while count<100:
##	print(str(count)+' :Type Ctrl-C to stop me!')
##	count +=1

x='spam'
while x:
        print(x)
        x = x[1:]

a = 0;b=10
while a<b:
        print(a)
        a+=1

while b:
        b=b-1
        if b%2 == 0:continue
        print(b)

pod = 1
List = [1,2,3,4,5,6]

str = 'jdkj'


for x in str:
        print(x,)

print(pod)


print('----------------------------------------------------')
T = [(1,2),(2,3),(3,4)]
for (a,b) in T:
        print (a+b)

file = open("data.txt",'rb')
while True:
        chunk = file.read(16)
        
        if not chunk:break
        print(chunk)

print('----------------------------------------------------')
for line in open("data.txt"):
        print(line)


print(list(range(-10,10)))
x="wenhuimeiling19890109109"
xrange = range(0,len(x),2)
for i in xrange:
        print(x[i],)

for i in x[::2]:
        print(i)


print('----------------------------------------------------')
L1 = [1,2,3,4,5]
L2 = [6,7,8,9,10]
L4 = ['a','b','c','d','e']
L3 = list(zip(L1,L2,L4))
dic = dict(zip(L1,L2))
print(dic)
print(L3)

print('----------------------------------------------------')
L = [x+10 for x in L1]
print(L)


file = open('data.txt')
lines= file.readlines()
print(lines)

lines2 = [line.rstrip() for line in lines]
print(lines2)
input()
