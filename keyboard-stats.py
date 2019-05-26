import os
import sys
from tabulate import tabulate

def read(f):
    return open(f).read().splitlines()

root_dir = sys.argv[1]
directories = read('./directories.txt')
filetypes = read('./filetypes.txt')
characters = read('./characters.txt')

def run():
    results = {key: 0 for key in characters}
    for dirpath, dirnames, files in os.walk(root_dir):
        for directory in directories:
            if dirpath.replace(root_dir + '/', '').startswith(directory):
                for file in files:
                    if os.path.splitext(file)[1] in filetypes:
                        for line in open(f'{dirpath}/{file}').readlines():
                            for char in characters:
                                results[char] = results[char] + line.count(char)
    return results

data = run()
print(tabulate(data.items(), headers=['Symbol', 'Count'], tablefmt='orgtbl'))
