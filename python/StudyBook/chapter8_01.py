dic = {'name':'wenhui','age':10,'ham':1,'egg':1111,10:10}
print(dic)

L=['Spam','spam','more','wenhui','please']
print(L)
L.sort()
print(L)
L.append('meiling')
L.append(100.0)
L.reverse()

print(L)

L.pop()
print(L)

del L[2:4]
print(L)

print(str(dic.values()))
print(dir(dic))
print('ham' in dic)
print (dic.items())

keylist = ['name','age']
vallist = ['wenhui','10']
dic2 = dict(zip(keylist,vallist))
print(dic2)

dic3 = dict(name='kaka',age=100)
print(dic3)

import cgi
form = cgi.FieldStorage()
if 'name' in form:
    showReply("hello," + form['name'].value)


#tuple examples
tu = (1,[2,4],10)
print(tu)
tu[1][1]='spam'
print(tu)

input()
