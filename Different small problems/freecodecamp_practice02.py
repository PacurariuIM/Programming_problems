# string extraction using regular expressions
import re

line = 'From stephen.marc@uct.ac.za Sat Jan 2008'
y = re.findall('^From .*@([^ ]*)', line)
print(y)
