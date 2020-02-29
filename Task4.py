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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
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

print(f"These numbers could be telemarketers: ")
print("\n".join(unique_nums)) # print on a new line
