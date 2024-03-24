import os,sys
filefolder = os.getcwd()
if len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print("commands syntex :","tee {write here} {path to file} :",end="" )
        print("open {filename} append file and print file to terminal")
if len(sys.argv) != 3:
    print("tee commands except 3 agrument but {} is given".format(len(sys.argv)))
else:
    message = sys.argv[1]
    filelocation = filefolder + f"/{sys.argv[2]}" 
    file = open(filelocation,"a")
    file.write(sys.argv[1])
    file.close()
    file = open(filelocation,'r')
    for i in file:
        print(i)
    file.close()