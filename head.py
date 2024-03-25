import os,sys
cwd = os.getcwd()
if len(sys.argv) == 2:
    if sys.argv[0] == "head.py" and sys.argv[1] == "--help":
        print("syntex of head commands : head { placeholder } {number} {filename}")
        print("placeholer = {-n} : For number of lines")
        print("placeholder = -b : For number of bytes")
        print("Uses of head command : to print in terminal  to the given number of lines,bytes")
        sys.exit()
if len(sys.argv) != 4:
    print("head commands except 4 argument but {} is given".format(len(sys.argv)))
number = sys.argv[2]
try:
    number = int(number)
except:
    sys.exit("head.py commands except 3 argument as type int. Please recheck it.")
placeholder = sys.argv[1]
filepath = cwd + f"/{sys.argv[3]}"
if placeholder != "-n":
    sys.exit("currently head commands except -n placeholder to print n line from top of file.  but {} is given".format(placeholder))
try:
    file = open(filepath,"r")
    for i,u in enumerate(file):
        if i >= number +1:
            break
        else:
            print(u)
    file.close()
except:
    sys.exit("filename or location is not correct. please check it")
    