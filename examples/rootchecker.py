import os 

def RootChecker():
    if os.getuid() != 0:
        print "Run as root, please"
