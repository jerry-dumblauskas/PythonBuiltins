import requests
from bs4 import BeautifulSoup
import sys

# pass in my name
nm = sys.argv[1]

# pass in id
l_id = sys.argv[2]

xx = requests.get('http://www.chipy.org/meetings/rsvp/list/' + l_id + "/", auth=('', ''))

my_file = nm + '/Downloads/wtf2.html'

file_handle = open(my_file, 'w')
file_handle.write(xx.text)

soup = BeautifulSoup(open(my_file), 'html.parser')
lst = ""
for x in soup.find_all('tr'):
    l_str = ""
    for y in x.find_all('td'):
        for zzz in y.stripped_strings:
            l_str = l_str + zzz + '\t'
    lst = lst + l_str + '\n'

my_file_out = nm + '/Downloads/wtf2.out'
l_file_out = open(my_file_out, 'w')
l_file_out.write(lst)
l_file_out.close()
