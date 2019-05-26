import os
import sys
from tabulate import tabulate

def read(f):
    return open(f).read().splitlines()

root_dir = sys.argv[1]
directories = read('./directories.txt')
filetypes = read('./filetypes.txt')
characters = read('./characters.txt')

def valid_path(path):
    for directory in directories:
        if path.replace(root_dir + '/', '').startswith(directory):
            return True
    return False

def valid_files(files):
    return (f for f in files if os.path.splitext(f)[1] in filetypes)

def run():
    results = {key: 0 for key in characters}
    for dirpath, dirnames, files in os.walk(root_dir):
        if not valid_path(dirpath):
            continue
        for file in valid_files(files):
            for line in read(f'{dirpath}/{file}'):
                for char in characters:
                    results[char] += line.count(char)
    return results

data = run()
print(tabulate(data.items(), headers=['Symbol', 'Count'], tablefmt='orgtbl'))
