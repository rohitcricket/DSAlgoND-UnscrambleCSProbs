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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A

bangSet = set()
for call in calls:
    # check if caller is from bangalore
    if call[0].startswith("(080)"):
      if call[1].startswith('(0'): # check if caller is from fixed line
        j = call[1].index(')')
        bangSet.add(call[1][:(j+1)])
      elif call[1].startswith('7'): # check if caller is from mobile
        bangSet.add(call[1][:4])
      elif call[1].startswith('8'): # check if caller is from mobile
        bangSet.add(call[1][:4])
      elif call[1].startswith('9'): # check if caller is from mobile
        bangSet.add(call[1][:4])


print(f"The numbers called by people in Bangalore have codes:")

sorted_bangs = sorted(bangSet)
print("\n".join(sorted_bangs))


# Part B

bang_calls = [call for call in calls if call[0].startswith("(080)")]

bang_dialed = [call[1] for call in bang_calls]

total_calls = len(bang_calls)

bang2bang = len([call for call in bang_calls if call[
    1].startswith("(080)")])

percent_calls = round(bang2bang / total_calls, 4) * 100

print("")
print(f"{percent_calls} percent of calls from fixed lines in Bangalore are calls "
      f"to other fixed lines in Bangalore.")
