import re

reg = re.compile(r'\S+\.?$')
myStr = 'AAA BBB CCC'
m = reg.search(myStr)
print(m.group())
