# PROJECT: FILE PROCESSING

import csv

with open('devices.txt', 'r') as f:
    devices_01 = list()
    for line in f:
        context = line.splitlines()
        devices_01.append(context)
        print(context)
print(devices_01)

with open('devices.txt', 'r') as f:
    devices_02 = list()
    for line in f:
        context = line.splitlines()
        context = context[0].split(':')
        devices_02.append(context)
        print(context)
print(devices_02)

with open('devices.txt', 'r') as f:
    devices_03 = list()
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print(row)
        devices_03.append(row)
print(devices_03)
