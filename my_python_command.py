import sys
while True:
    value1 = input()
    if sys.argv[1] in value1:
        print(value1)
    else:
        print("not found")
