import os
import sys

root_dir = sys.argv[1]
directories = open('./directories.txt').read().splitlines()

for dirpath, dirnames, files in os.walk(root_dir):
    for directory in directories:
        if dirpath.replace(root_dir + '/', '').startswith(directory):
            print(dirpath)
            print(files)
