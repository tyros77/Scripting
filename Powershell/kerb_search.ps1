# Author: tyros77
# Script to parse DC security log for TGS requests to identify Kerberos attacks
# cpname - the name of the server
# t = number of hours to go back in log from current time
# start - where it starts in the log file (current time - t)

$cpname = $args[0]
$t = $args[1]
$start = (Get-Date).AddHours(-$t)
$properties = @(
	@{n='EventID';e={$_.ID}}
	@{n='Date';e={$_.TimeCreated}}
	@{n='AccountName';e={$_.Properties[0].Value}}
	@{n='ServiceName';e={$_.Properties[2].Value}}
	@{n='Encryption';e={$_.Properties[5].Value | Format-Hex | Select-Object -Expand Bytes | ForEach-Object { '0x{0:x2}' -f $_ } -join ''}})
Get-WinEvent -ComputerName $cpname -FilterHashTable @{LogName='Security'; ID=4769; StartTime=$start} | Select-Object $properties | Format-Table -AutoSize
