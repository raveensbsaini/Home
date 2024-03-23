import os,sys
a = os.getcwd()
if len(sys.argv) != 3:
    print("tee commands except 3 agrument but {} is given".format(len(sys.argv)))
