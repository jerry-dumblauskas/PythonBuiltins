__author__ = 'jerrydumblauskas'
'''
This script was sent to me by a junior dev, and illustrates an issue
that should be easy to solve, but I didn't see one.  u' is put in front
of all the strings, which turns out is to spec, but when used to load data into
a csv this is messy.  The version of python here is 2.6.  The tactical
solution was using object_hook in the json.load and casting all
unicode types to str (which I will commit later).  But there should be a cleaner
way to do this, as I have to imagine this quite a common request
'''
import csv, json, sys

input = open(sys.argv[1])
data = json.load(input)
input.close()

output = csv.writer(sys.stdout, dialect=csv.excel)

output.writerow(data[0].keys())  # header row

for row in data:
    output.writerow(row.values())

# tactical fix -- custom object hook in json.load
# I don't like this approach and need to find a better way
def dict_to_object(d):
    rtn={}
    for key in d.keys():
        m_val = d[key]
        if isinstance(m_val, unicode):
            m_val = str(m_val)

        rtn[str(key)] = m_val

    return rtn

input = open(sys.argv[1])
data = json.load(input, object_hook=dict_to_object)
input.close()

output = csv.writer(sys.stdout)

output.writerow(data[0].keys())  # header row


for row in data:
	output.writerow(row.values())