#! /usr/bin/python
import os
from time import ctime

def findIP(targetFolder):
    Result = {}
    IP = {}
    for root, dirs, files in os.walk(targetFolder):
        for f in files:
            # read small files
            file_handler = open(os.path.join(targetFolder, f), 'r')
            lines = file_handler.readlines()
            file_handler.close()
            # get IP in file, store to IP Dictionary
            for line in lines:
                if line in IP:
                    IP[line] = IP[line] + 1
                else:
                    IP[line] = 1
            # sort Dictionary
            # print IP.items()
            IP = sorted(IP.items(), key=lambda d: d[1])
            # get max item(s), store to Result Dictionary
            maxItem = IP[-1][1]
            print '  File ' + str(f) + ":"
            print "    maxItem: " + str(IP[-1])
            tempTuple = IP.pop()
            while tempTuple[1] == maxItem:
                if tempTuple[0] in Result:
                    Result[tempTuple[0]] = Result[tempTuple[0]] + 1
                else:
                    Result[tempTuple[0]] = tempTuple[1]
                tempTuple = IP.pop()
            IP = {}
            print '    Finished: ' + ctime()
                    
    print sorted(Result.items(), key=lambda d: d[1])

if __name__ == '__main__':
    print 'Start: ' + ctime()
    findIP("massiveData")
    print 'End: ' + ctime()
