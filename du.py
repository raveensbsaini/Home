import sys,os
filepath = os.getcwd()
# print(filepath)
if len(sys.argv) != 2:
    sys.exit("du.py commands except 2 argument but {} is Given.".format(len(sys.argv)))
if sys.argv[0] != "du.py":
    sys.exit("first commands argument must be du.py but {} is given.".format(sys.argv[0]))
filepath += "/{}".format(sys.argv[1])
if sys.argv[1][0] == "/":
    filepath = sys.argv[1]
# print(filepath)
file = open(filepath,"rb")
count = 0
while file.read(1):
    count += 1
print(count,"bytes     ",sys.argv[1])