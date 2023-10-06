# check_space 
# Check diskspace in diffrent size types
# 2023 Anders Persson
# MIT Licence

import shutil
import math
import sys

def translate_type_size(stat,size_type):
    match size_type.upper():
        case "KB":
            SIZE_CONST = 1024
        case "MB":
            SIZE_CONST = 1048576
        case "GB":
            SIZE_CONST = 1073741824
        case "TB":
            SIZE_CONST = 1099511627776
    return {"total":round(stat.total / SIZE_CONST,2),"free": round(stat.free / SIZE_CONST,2), "used":round(stat.used / SIZE_CONST,2)}

def main():    
    if( len(sys.argv) < 2):
            print("Help!")
            print("check_space.py <KB|MB|GB|TB> Path")
            print("Example:\ncheck_space.py MB /home")
            exit()

    args = sys.argv[1:]

    size_type = "KB" # Default type
    if( len(args) > 1):
        size_type = args[0]
        path = args[1]

    stat = shutil.disk_usage(path)
    disk_stat = translate_type_size(stat,size_type)
    print( disk_stat )
    used_p = math.floor((disk_stat["used"] / disk_stat["total"] ) * 100)
    left_p = 100 - used_p

    # Print disk usage statistics
    print("Disk usage statistics:")
    print(f"Free:  {disk_stat['free']:>10} {size_type}")
    print(f"Used:  {disk_stat['used']:>10} {size_type}")
    print(f"Total: {disk_stat['total']:>10} {size_type}")
    print(f"Used:  {used_p:>10} %")
    print(f"Left:  {left_p:>10} %")

if __name__ == "__main__":
    main()

