import os,sys
cwd = os.getcwd()
if len(sys.argv) != 2:
    print("cat.py command except 2 argument but {} was given".format(len(sys.argv)))
else:
    filepath = cwd + "/" +sys.argv[1]
    file = open(filepath,"r")
    for i in file:
        print(i)
    file.close()