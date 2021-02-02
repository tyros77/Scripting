# Author: tyros77
# Script to parse the security log on DC for specific event id's
# cpname - name of the server
# id - event id(s) to search for, can use multiple with this format: 4897,4769,4768
# t = number of hours to go back in log from current time
# start - where it starts in the log file (current time - t)

$cpname = $args[0]
$id = $args[1]
$t = $args[2]
$start = (Get-Date).AddHours(-$t)
Get-WinEvent -ComputerName purpDC01 -FilterHashTable @{LogName='Security'; ID=$id; StartTime=$start}
