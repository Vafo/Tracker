from curses.ascii import isascii
import enum
import os

def read_bin(filename: str):
    print('BINARY CONTENT OF ' + filename)
    size = os.stat(filename).st_size
    print('SIZE OF FILE ' + str(size))

    with open(filename, "rb") as file:
        row = file.read(16)
        big = 2 << 28
        prev_size = 0
        while row:
            print(hex(big + prev_size)[3:] + ': ', end='')
            prev_size += len(row)

            
            str_content = '     |'

            delim = ['', ' ']
            i = 0
            for byte in row:
                out = hex(byte + 256)[3:]
                print(out, end=delim[i])
                i ^= 1

                ch = chr(byte)
                if ch.isascii() and ch.isprintable():
                    str_content += ch
                else:
                    str_content += '.'

            str_content += '|'
            
            print(str_content)
            row = file.read(16)

# Prints content of local files with extension .sdocx
working_dir = os.getenv("pwd")
print(working_dir)

aboba = os.scandir(working_dir)

todos = []

for f in aboba:
    _, ext = os.path.splitext(f)
    if f.is_file() and ext == ".sdocx":
        todos.append(os.path.abspath(f))

for idx, el in enumerate(todos):
    print(idx, el)
choice = int(input())
#read_bin(todos[choice])
read_bin('text.txt')