# Author: tyros77
# Simple program that dumps the ELF file header and pulls out information about it

#!/usr/bin/python3

import sys

formatlist = (['01','32 bit'], ['02','64 bit'])
endianlist = (['01','little'], ['02','big'])
machinelist = (['02','SPARC'], ['03','x86'], ['08','MIPS'], ['14','PowerPC'], ['28','ARM'], ['2a','SuperH'], ['32','IA-64'], ['3e','amd64'], ['b7','AArch64'], ['f3','RISC-V'])
fh = open(sys.argv[1], "rb")
print(f"File     : {sys.argv[1]}")
magic = fh.read(4).hex() #reads binary file then converts bits to hex
print(f"Magic    : 0x{magic}")
format = fh.read(1).hex()
for count in formatlist:
    if format in count:
        print(f"Format   : {count[1]}")
endian = fh.read(1).hex()
for count in endianlist:
    if endian in count:
        print(f"Endian   : {count[1]}")
fh.seek(18,0)
machine = fh.read(1).hex()
for count in machinelist:
    if machine in count:
        print(f"Machine  : {count[1]}")
fh.close()
