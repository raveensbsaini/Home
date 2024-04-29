import os,sys
from pathlib import Path
filepath = os.getcwd()
if len(sys.argv) < 2:
    sys.exit("tee.py command except 2 or more than two commands.")
filepath += "/{}".format(sys.argv[1])
if len(sys.argv) == 2:
    if sys.argv[0] != "tee.py":
        sys.exit("1st command argument must be tee.py but {} is given.".format(sys.argv[0]))
    file = open(filepath,"a")
    for line in sys.stdin:
        file.write(line)
    file.close()
    sys.exit("success")
if len(sys.argv) == 3:
    if sys.argv[0] != "tee.py":
        sys.exit("1st comman argument must be tee.py but {} is given ".format(sys.argv[0]))
    try:
        file = open(filepath,"a")
    except:
        sys.exit("cannot find file {}".format(sys.argv[1]))
    pattern = sys.argv[2]
    # file.write("\n")
    file.write(pattern)
    file.write("\n")
    file.close
    file = open(filepath,"r")
    for i in file:
        print(i,end="")
    file.close()
