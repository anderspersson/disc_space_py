# Python program to explain shutil.disk_usage() method

# importing shutil module
import shutil
import math
import sys

def TranslateTypeSize(stat,sizeType):

    match sizeType.upper():
        case "KB":
            adj = 1024
        case "MB":
            adj = 1048576
        case "GB":
            adj = 1073741824
        case "TB":
            adj = 1099511627776
    stat.total = stat.total / adj
    stat.free = stat.free / adj
    stat.used = stat.used / adj
    return stat

def main():    
    if( len(sys.argv) < 2):
            print("check_space.py SizeType Path")
            print("Example:\ncheck_space.py MB /home")
            exit()

    args = sys.argv[1:]

    SizeType = "Bytes" # Default type
    if( len(args) > 1):
        SizeType = args[0]
        path = args[1]

    stat = shutil.disk_usage(path)
    # stat = TranslateTypeSize(stat,SizeType)
    used_p = math.floor((stat.used /stat.total ) * 100)
    left_p = 100 - used_p

    # Print disk usage statistics
    print("Disk usage statistics:")
    print(f"Total: {stat.total} {SizeType}")
    print(f"Free: {stat.free} {SizeType}")
    print(f"Used: {stat.used} {SizeType}")
    print(f"Used: {used_p} %")
    print(f"Left: {left_p} %: ")
    print(stat)



main()

