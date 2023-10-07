# check_space 
# Check diskspace in diffrent size types
# 2023 Anders Persson
# MIT Licence

import shutil
import math
import sys
import argparse

parser = argparse.ArgumentParser(description="check_space",
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--type", choices=['KB', 'MB', 'GB', 'TB'], help="Size Type")
parser.add_argument("-s", "--silent", action="store_true", help="Only numbers in result")
parser.add_argument("path", help="Drive and/or path")
args = parser.parse_args()
config = vars(args)

def translate_type_size(stat,size_type):
    match str(size_type).upper():
        case "KB":
            SIZE_CONST = 1024
        case "MB":
            SIZE_CONST = 1048576
        case "GB":
            SIZE_CONST = 1073741824
        case "TB":
            SIZE_CONST = 1099511627776
        case _:
            SIZE_CONST = 1

    return {"total":round(stat.total / SIZE_CONST,2),"free": round(stat.free / SIZE_CONST,2), "used":round(stat.used / SIZE_CONST,2)}

def main():    
    if config["help"] == True:
        help = """
        check_space for checking diskspace
        Argument
        -t, --type type to convert result to KB, MB, TB.
        -s, --silent Only number in result.
        path Drive and/or path.

        Example:
        python .\check_space.py c:\
        python .\check_space.py -t GB c:\
        python .\check_space.py -t GB -v c:\
        """
        print(help)
        exit()

    stat = shutil.disk_usage(config["path"])
    disk_stat = translate_type_size(stat,config["type"])
    used_p = math.floor((disk_stat["used"] / disk_stat["total"] ) * 100)
    left_p = 100 - used_p

    if config["silent"] == true:
        print(disk_stat['free'])
        exit()

    # Print disk usage statistics
    print("Disk usage statistics:")
    if config["type"] == None:
        config["type"] = "Byte"
    print(f"Free:  {disk_stat['free']:>10} {config['type']}")
    print(f"Used:  {disk_stat['used']:>10} {config['type']}")
    print(f"Total: {disk_stat['total']:>10} {config['type']}")
    print(f"Used:  {used_p:>10} %")
    print(f"Left:  {left_p:>10} %")

if __name__ == "__main__":
    main()

