from datetime import datetime 
from datetime import date
from datetime import timedelta 
import os
import sys

date_format = "%Y-%m-%d"
dt = timedelta(days=1)

beginning_sys_arg = (datetime.today() - dt).strftime(date_format)
ending_sys_arg = datetime.today().strftime(date_format)
for argument in sys.argv:
    if "--start=" in argument:
        beginning_sys_arg = argument[8:]
    elif "--end=" in argument:
        ending_sys_arg = argument[6:]
    elif "--" in argument:
        print("Sorry, I can only take arguments for beginning and ending by --start=yyyy-mm-dd and --end=yyyy-mm-dd")
        exit()

beginning_date = datetime.strptime(beginning_sys_arg, date_format)
ending_date = datetime.strptime(ending_sys_arg, date_format)
time_interval = ending_date - beginning_date
for num_days in range(0, time_interval.days):
    generating_date = beginning_date + dt * num_days
    folder = str(generating_date.year) + "." + str(generating_date.month)
    filename = folder + "/" + generating_date.strftime(date_format).replace('-0', '-') + "-muse.md"
    if not os.path.isfile(filename):
        with open(filename, "w") as new_musing:
            new_musing.write('---\nlayout: post\ncomments: true\ntitle:  ""\ndate:   ' + generating_date.strftime(date_format).replace('-0','-') + ' 00:00:00\nhidden: true\ncategory: "Musing"\n---')
    else:
        print("Ignoring already made file: " + filename)
