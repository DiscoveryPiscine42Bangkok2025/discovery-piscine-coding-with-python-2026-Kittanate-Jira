import sys

if len(sys.argv) == 3:
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    my_list = list(range(start, end + 1))

    print(my_list)
else:
    print("none")