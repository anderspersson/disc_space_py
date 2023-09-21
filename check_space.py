# Python program to explain shutil.disk_usage() method

# importing shutil module
import shutil
import math
import sys


path = "/"

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
used_p = math.floor((stat.used / stat.free) * 100)
left_p = 100 - used_p

# Print disk usage statistics
print("Disk usage statistics:")
print(f"Free: {stat.free} {SizeType}")
print(f"Used: {stat.used} {SizeType}")
print(f"Used: {used_p} %")
print(f"Left: {left_p} %: ")


#1 KB = 1,024 Bytes
#1 MB = 1024KB = 1,048,576 Bytes
#1 GB = 1024MB = 1,048,576 KB = 1,073,741,824 Bytes
#1 TB = 1024 GB = 1,048,576 
#MB = 8,388,608 KB = 1,099,511,627,776 Bytes
