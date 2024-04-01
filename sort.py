import sys,os,colorama,collections
cwd = os.getcwd()
if len(sys.argv) == 2:
    if sys.argv[0] == "sort.py":
        filepath = cwd + "/" + sys.argv[1]
        d = collections.defaultdict(list)
        try:
            with open(filepath,"r") as file:
                line_list = []
                for i in file:
                    line_list.append(i)
                line_list.sort()
                for i in line_list:
                    print(i,end="")
        except:
            sys.exit("No such file or directory")