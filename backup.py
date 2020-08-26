import json
from pyntc import ntc_device as NTC
import getpass

f = open('iplist.txt', 'r')

hosts = f.read()
hosts = hosts.split()

pw = getpass.getpass()
for each in hosts:
	try:
		file = open(each+".txt", "w+")
		print("\n", each, "-- writing backup locally")
		x = NTC(host=each, username='dtroxler', password=pw, device_type='cisco_ios_ssh')
		backup = x.running_config
		file.write(backup)
	except:
		print(each, " FAILED")
