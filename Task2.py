"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    



"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_spent = {}
for value in calls:
    if value[0] in time_spent:
        time_spent[value[0]] += int(value[3])
    else:
        time_spent[value[0]] = int(value[3])
    if value[1] in time_spent:
        time_spent[value[1]] += int(value[3])
    else:
        time_spent[value[1]] = int(value[3])

longest_time = max(time_spent,key=lambda x:time_spent[x])
print(f'{longest_time} spent the longest time, {time_spent[longest_time]} seconds, on the phone during September 2016')
