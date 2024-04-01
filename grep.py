import os,sys
from pathlib import Path
from colorama import Fore, Back, Style
print("This commands is made by Ravindra kumar saini")
count = 1
def check(string,pattern,dict):
    c = False
    for i,u in enumerate(string[:len(string)-len(pattern)]):
        if string[i:i+len(pattern)] == pattern:
            c = True
            for i in range(i,i+len(pattern)):
                dict[i] = True
    return c
if len(sys.argv) == 2:
    if sys.argv[1] != "--help":
        count = 1
        for line in sys.stdin:
            pattern = sys.argv[1]
            d = {}
            if check(line,pattern,d):
                print(Fore.BLUE + f"{count} ",end="")
                for idx,value in enumerate(line):
                    if idx not in d:
                        print(Fore.GREEN+ value,end="")
                    else:
                        print(Fore.RED + value,end="")
            count += 1
if len(sys.argv) == 3:
    if sys.argv[0] == "grep.py":
        pattern = sys.argv[1]
        cwd  = os.getcwd()
        filepath = cwd + "/" + sys.argv[2]
        count = 1
        print(filepath)
        with open(filepath,"r") as file:
            for i in file:
                empty_dict = {}
                if check(i,pattern,empty_dict):
                    print(Fore.BLUE + f"{count} ",end='')
                    for idx,value in enumerate(i):
                        if idx not in empty_dict:
                            print(Fore.GREEN+ value,end="")
                        else:
                            print(Fore.RED + value,end="")
                count += 1
    