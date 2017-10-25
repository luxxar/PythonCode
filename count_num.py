import re

print sum(int(s) for s in re.findall('[0-9]+', open("regex_sum_44615.txt", mode='r').read()))
