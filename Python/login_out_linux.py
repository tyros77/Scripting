# Author: tyros77
# Displays user login/logout info for Linux

#!/usr/bin/python3

import os
newlist = []
fh = os.popen('last -f /var/log/wtmp')
data = fh.read()
info = data.split('\n')
for x in info:
    if 'reboot' in x:
        continue
    elif 'wtmp' in x:
        continue
    else:
        newlist.append(x)
for x in range(len(newlist)):
    print(newlist[x][39:64]," ",newlist[x][0:8]," ",newlist[x][22:39]) #tip from Ian on how to format this output
