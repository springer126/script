List = [1,2,3,4,5,6,7,8,9]
for i in List:
    i = i*2
    print(i)

while True:
    reply = input('Enter your number:')
    if reply == 'Stop':
        break
    elif not reply.isdigit():
        print('Bad!'*8)

    else:
        reply = int(reply)
        print(reply**2)

print(list(range(10)))


if 1:
    print(True)
else:
    print(False)

print(0<1<1)
print([] or {})
input()
