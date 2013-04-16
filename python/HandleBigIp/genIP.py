#! /usr/bin/python

def genRandom(From,To):
    import random
    return random.randint(From,To)

def generageMassiveIPAddr(fileLocation,numberOfLines):
    IP = []
    file_handler = open(fileLocation, 'a+')
    for i in range(numberOfLines):
        IP.append('10.197.' + str(genRandom(0,255))+'.'+ str(genRandom(0,255)) + '\n')

    file_handler.writelines(IP)
    file_handler.close()

if __name__ == '__main__':
    from time import ctime
    print ctime()
    generageMassiveIPAddr('massiveIP.txt', 10000000)
    print ctime()
