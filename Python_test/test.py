import re

myStr = '新北市三重區'
myStr2 = 'abcde'

is_english_name = re.compile(r'^([a-zA-Z0-9_,\. ]*)$')
is_english_name = re.compile(r'^([\w,\. ]*)$')

m = is_english_name.search(myStr)
print(m)
print(m.group())
