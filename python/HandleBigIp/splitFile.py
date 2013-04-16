#! /usr/bin/python

from time import ctime
def splitFile(fileLocation, targetFoler):
    file_handler = open(fileLocation, 'r')
    block_size = 1000000
    line = file_handler.readline()
    temp = []
    countFile = 1
    while line:
		temp.append(line)
        for i in range(block_size):
            if i == (block_size-1):
                file_writer = open(targetFoler + "/file_"+str(countFile)+".txt", 'a+')
                file_writer.writelines(temp)
                file_writer.close()
                temp = []
                countFile = countFile + 1
            else:
                temp.append(file_handler.readline())
	line = file_handler.readline()
    file_handler.close()

if __name__ == '__main__':
    print "Start At: " + str(ctime())
    splitFile("massiveIP.txt", "massiveData")
