# Python program to explain shutil.disk_usage() method

# importing shutil module
import shutil
import math
import sys

# Path
path = "/"

args = sys.argv[1:]

SizeType = "Bytes" # Default type
if( len(args) < 0):
    SizeType = args[0]

stat = shutil.disk_usage(path)
used_p = math.floor((stat.used / stat.free) * 100)
left_p = 100 - used_p

# Print disk usage statistics
print("Disk usage statistics:")
print(f"Free: {stat.free} {SizeType}")
print(f"Used: {stat.used} {SizeType}")
print(f"Used: {used_p} %")
print(f"Left: {left_p} %: ")

