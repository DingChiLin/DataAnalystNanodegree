import dns.resolver

domain = 'post.mipt.ru'
#domain = 'mipt.ru'

domain = '.'.join(domain.split('.')[1:])
print(domain)
try:
    dns.resolver.query(domain,'MX')
    print('YES')
except:
    print('NO')
