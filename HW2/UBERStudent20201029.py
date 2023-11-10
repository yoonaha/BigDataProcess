#!/usr/bin/python3
import sys
from datetime import datetime

input_file = sys.argv[1]
output_file = sys.argv[2]

uberList = []

with open(input_file, 'r', encoding = 'utf-8') as fp:
    data = fp.read()

    rows = data.split("\n")
    for row in rows:
        fields = row.split(',')
        base_number = fields[0]
        date = fields[1]
        active_vehicles = int(fields[2])
        trips = int(fields[3])
        
        dateTime = datetime.strptime(date, "%m/%d/%Y")
        day = dateTime.weekday()
        week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"][day]

        found = False
        for list in uberList:
            if list[0] == base_number and list[1] == week:
                list[2] += active_vehicles
                list[3] += trips
                found = True
                break

        if not found:
            uberList.append([base_number, week, active_vehicles, trips])

with open(output_file, 'w', encoding = 'utf-8') as fp:
    for list in uberList:
        fp.write(f"{list[0]},{list[1]} {list[2]},{list[3]}\n")