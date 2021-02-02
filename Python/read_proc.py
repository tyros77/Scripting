# Author: tyros77
# A script to reads information from /proc/<PID>/stat

#!/usr/bin/python3
import sys

class LinuxProcess:
    def __init__(self, file1):
        try:
            self.fh = open("/proc/" + file1 + "/stat", "r")
            self.contents = self.fh.read()
            self.list = self.contents.split(" ")
            self.fh.close()
        except:
            print('PID does not exist')
            sys.exit()
    def getname(self):
        return self.list[1]
    def getpid(self):
        return self.list[0]
    def getppid(self):
        return self.list[3]
    def getrss(self):
        return hex(int(self.list[23]))
    def getrsslim(self):
        return hex(int(self.list[24]))
    def getstartcode(self):
        return hex(int(self.list[25]))
    def getendcode(self):
        return hex(int(self.list[26]))
    def getstack(self):
        return hex(int(self.list[27]))
    def getstartdata(self):
        return hex(int(self.list[44]))
    def getenddata(self):
        return hex(int(self.list[45]))
    def getstartbrk(self):
        return hex(int(self.list[46]))
    def getargstart(self):
        return hex(int(self.list[47]))
    def getargend(self):
        return hex(int(self.list[48]))
    def getenvstart(self):
        return hex(int(self.list[49]))
    def getenvend(self):
        return hex(int(self.list[50]))
        
file1 = sys.argv[1]
LinuxProcess1 = LinuxProcess(file1)
print("name: ", LinuxProcess1.getname().rjust(5, ' '))
print("pid: ", LinuxProcess1.getpid().rjust(5, ' '))
print("ppid: ", LinuxProcess1.getppid().rjust(5, ' '))
print("rss: ", LinuxProcess1.getrss().rjust(5, ' '))
print("rsslim: ", LinuxProcess1.getrsslim().rjust(5, ' '))
print("start_code: ", LinuxProcess1.getstartcode().rjust(5, ' '))
print("end_code: ", LinuxProcess1.getendcode().rjust(5, ' '))
print("start_stack: ", LinuxProcess1.getstack().rjust(5, ' '))
print("start_data: ", LinuxProcess1.getstartdata().rjust(5, ' '))
print("end_data: ", LinuxProcess1.getenddata().rjust(5, ' '))
print("start_brk: ", LinuxProcess1.getstartbrk().rjust(5, ' '))
print("arg_start: ", LinuxProcess1.getargstart().rjust(5, ' '))
print("arg_end: ", LinuxProcess1.getargend().rjust(5, ' '))
print("env_start: ", LinuxProcess1.getenvstart().rjust(5, ' '))
print("env_end: ", LinuxProcess1.getenvend().rjust(5, ' '))
