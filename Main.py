import os
import tkinter as tk

def format_bytes(b):
    if b < 1000:
              return '%i' % b + 'B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b/1000) + 'KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b/1000000) + 'MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b/1000000000) + 'GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b/1000000000000) + 'TB'


def folderSizeNUM(folder):
    size = 0
    try:
        scanner = os.scandir(folder)
    except:
        scanner = ''
    for entry in scanner:
        if entry.is_file():
            size += os.path.getsize(entry)
        elif entry.is_dir():
            size += folderSizeNUM(entry)
    return size


def folderSize(folder):
    size = 0
    scanner = os.scandir(folder)
    for entry in scanner:
        if entry.is_file():
            size += os.path.getsize(entry)
        elif entry.is_dir():
            size += folderSizeNUM(entry)
    print(format_bytes(size))

result = []
path = "\\"

obj = os.scandir(path)

print(f'Files and Directories in {path}:')


for entry in obj:
    if entry.is_dir() and entry.name[0] != '$':
        try:
            test = entry.path()
        except TypeError:
            test = path + entry.name
        try:
            temp = folderSizeNUM(path + entry.name)
            result.append(str(entry.name) + " " + str(format_bytes(temp)))
            print(str(entry.name) + " " + str(format_bytes(temp)))
        except PermissionError:
            result.append(f'{str(entry.name)}  (Size unavailable)')
            print(f'{str(entry.name)}  (Size unavailable)')

obj.close()
