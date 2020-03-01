"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

senders_texts = []
receivers_texts = []

for i in range(len(texts)):
    senders_texts.append(texts[i][0])
    receivers_texts.append(texts[i][1])

texters = list(set(senders_texts).intersection(set(receivers_texts)))

senders_calls = []
receivers_calls = []

for i in range(len(calls)):
    senders_calls.append(calls[i][0])
    receivers_calls.append(calls[i][1])

callers = list(set(senders_calls).intersection(set(receivers_calls)))

unique_nums = list(set(texters).intersection(set(callers)))
count = len(unique_nums)

print(f"There are {count} different telephone numbers in the records.")