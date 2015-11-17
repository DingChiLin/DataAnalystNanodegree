import re

str = '1.5}'

def is_float(num):
    try:
        i = float(num)
        return i
    except ValueError:
        return False

def is_int(num):
    try:
        i = int(num)
        return i
    except ValueError:
        return False

print(is_int(str))
print(is_float(str))

def is_list(data):
    reg = re.compile(r'{.*}')
    m = reg.search(data)
    return False if m == None else True

print(is_list(str))

print(type(1.1))

if 
if type(1.1) == 'float':
    print("YES")

