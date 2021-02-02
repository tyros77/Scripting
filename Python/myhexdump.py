# Author: tyros77
# Simple hex dump program in python completed as a school project

#!/usr/bin/python3

import sys, os

fh = open(sys.argv[1], 'rb')

def hexdump(start):
    offset = start
    for count in range(6):
        contents = fh.read(16)
        hexa = contents.hex()
        decim = list(contents)
        print(f"[{format(offset, 'x').rjust(8, '0')}]", end=" ")
        if len(hexa) != 32:
            diff = 32-len(hexa)
            buff = '00'*int((diff/2))
            hexa = hexa + buff
        for x in range(0,len(hexa),2):
            print(hexa[x:(x+2)], sep='', end=' ')
        print(' ', end='')
        if len(decim) != 16:
            diff = 16-len(decim)
            for x in range(diff):
                decim.append(0)
        for item in decim:
            if 33 < item < 126:
                print(chr(item), sep='', end='') 
            else:
                print('.', sep='', end='')
        offset += 16
        print('', end='\n')
    print('Total length ', offset)
    return offset
    
newoff = hexdump(0)
size = os.path.getsize(sys.argv[1])
size1 = int(size/16)
for x in range(size1):
    user = input('Continue = c, Quit = q: ')
    if user == 'c':
        newoff = hexdump(int(newoff))
    elif user == 'q':
        sys.exit()
    else:
        print('Invalid syntax')
        sys.exit()
