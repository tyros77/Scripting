# Author: tyros77
# This script gets all running processes from /proc and creates an internal structure process tree

#!/usr/bin/python3
import os, sys
class color:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    end = '\033[0m'
class LinuxProcList:
    def __init__(self):
        try:
            self.processes = [pid for pid in os.listdir('/proc') if pid.isdigit()]
        except:
            print('Cant open file path')
            sys.exit()
    def getrange(self):
        return len(self.processes)
    def getpid(self, x):
        return self.processes[x]
    def getcmdline(self, y):
        self.command = []
        for x in self.processes:
            self.fh = open("/proc/" + x + "/cmdline", "r")
            self.contents = self.fh.read()
            if self.contents == '':
                self.command.append('None')
            else:
                self.command.append(self.contents)
            self.fh.close()
        return self.command[y]
    def getchildren(self, w):
        self.children = []
        for x in self.processes:
            self.fh = open("/proc/" + x + "/task/" + x + "/children", "r")
            self.contents = self.fh.read()
            if self.contents == '':
                self.children.append('None')
            else:
                self.children.append(self.contents)
            self.fh.close()
        return self.children[w]
    def getprintline(self, x):
        if int(self.processes[x]) > 999:
            print('    |')
            print('    ---->', end=' ')
        elif 99 < int(self.processes[x]) < 1000:
            print('   |')
            print('   ---->', end=' ')
        elif 9 < int(self.processes[x]) < 100:
            print('  |')
            print('  ---->', end=' ')
        elif int(self.processes[x]) < 10:
            print(' |')
            print(' ---->', end=' ')
LinuxProclist1= LinuxProcList()
for x in range(0, LinuxProclist1.getrange()):
    print(color.red, LinuxProclist1.getpid(x), color.end)
    LinuxProclist1.getprintline(x)
    print(color.blue, LinuxProclist1.getcmdline(x), color.end)
    LinuxProclist1.getprintline(x)
    print(color.green, LinuxProclist1.getchildren(x), color.end)
