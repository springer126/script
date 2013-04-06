import sys
print ('Hello World')
print (2**100)
title = "The meaning of life"


s="abcdefghijk/0/t/n"
print (s)
print (len(s))

import re
match = re.match("hello[\t]*(.*)world","wenhui,hello    python world")
#print (match.group(1))


L = ['wenhui',1233,87.91]
print (L)
L.append('meiling')
print (L)
#print (dir(L))
print (L.pop(2))
#Line = ['abc','bcd','des','aef']
#Line = [100,90,'wenhui',11] #字符串和数值比较抛出异常
Line = [100,90,0,11]
Line.sort()
print (Line)

print ('嵌套')
M=[[1,2,3],[4,5,6],[7,8,9]]
col1 = [row[1]*10+8 for row in M if row[1]%2==0]
print(col1)
diag = [M[i][i] for i in [0,1,2]]
print (diag)
print (M)


doubles = [c*2 for c in 'spam']
print(doubles)

print('字典')
D={'name':'wenhui','age':'10','color':'red'}
print(D)
print(D['name'])
Dic={}
Dic['name']={'first':'meiling','last':'cheng'}
Dic['age']=200
Dic['home']='huangshan'
print(Dic)
print(Dic['name']['last'])
Dic['job']=['student']
Dic['job'].append('janitor')
print(Dic['job'])

ks = Dic.keys()
#ks.sort()
for key in ks:
    print(key ,'=>',Dic[key])
print()
for key in sorted(Dic):
    print(key ,'=>',Dic[key])

print()
square = [x**2 for x in [1,2,3,4,5,6,7,8,9]]
print(square)

print('文件核心类型')
f= open('data.dat','w')
f.write('hello world\n')
f.close()

f=open('data1.dat','r')
bytes = f.readline()
print(bytes)

#import fibo
#print(fibo.fib(1000000))

a=3.0
b=4.0
print(a+10,b**2)
print(a/(b+3.0))
print(repr(1/3.0))
print(str(1/3.0))

print()
x=1
print(x<<2)
print(x | 2)

import math
print(dir(math))
import random
print(random.randint(1,10))
i = 0
while i<100:
    print(random.randint(1,100)); i = i+1
input()
