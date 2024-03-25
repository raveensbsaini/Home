import os,sys
cwd = os.getcwd()
if len(sys.argv) == 2:
    if sys.argv[0] == "tail.py" and sys.argv[1] == "--help":
        print("syntex of tai..py commands : tail.py { placeholder } {number} {filename}")
        print("placeholer = {-n} : For number of lines")
        print("placeholder = -b : For number of bytes")
        print("Uses of tail.py command : to print in terminal  to the given number of lines,bytes")
        sys.exit()
if len(sys.argv) != 4:
    print("tail.py commands except 4 argument but {} is given".format(len(sys.argv)))
number = sys.argv[2]
try:
    number = int(number)
except:
    sys.exit("tail.py commands except 3 argument as type int. Please recheck it.")
placeholder = sys.argv[1]
filepath = cwd + f"/{sys.argv[3]}"
if placeholder != "-n":
    sys.exit("currently tail.py commands except -n placeholder to print n line from top of file.  but {} is given".format(placeholder))
try:
    file = open(filepath,"r")
    leng = 0
    for i in file:
        leng += 1
    file.close()
    file = open(filepath,"r")
    for i,u in enumerate(file):
        if i >= leng - number:
            print(u)
    file.close()
except:
    sys.exit("filename or location is not correct. please check it")