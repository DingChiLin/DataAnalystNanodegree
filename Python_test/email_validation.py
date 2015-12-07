#Although there are lots of redundant loops, it's easy to debug and make change, and the data volume is small, so I left it this way.
import string
import dns.resolver

remove = '"(),:;<>[] '

import csv

#Basic import and parse
with open('emails_cn.csv', 'rb') as f:
    reader = csv.reader(f)
    emails = map(lambda x:x[0].decode("utf8").encode('ascii','ignore').strip().strip('.').translate(None, remove).lower(), list(reader))

#delete duplicate email
emails = sorted(set(emails), key=lambda x: emails.index(x))
print(len(emails))

#check if there is only one @ and split out domain
emails = filter(lambda x:len(x.split('@'))==2, emails)
print(len(emails))

#find unique domain
domains = map(lambda x:x.split('@')[1], emails)
domains = sorted(set(domains), key=lambda x: domains.index(x))

print(len(domains))

#find valid domain
valid_domains = []
invalid_domains = []

for idx, domain in enumerate(domains):
    print idx
    try:
        dns.resolver.query(domain, 'MX')
        valid_domains.append(domain)
    except:
        invalid_domains.append(domain)

print valid_domains
print invalid_domains

#find email with valid domain
f_valid = open('valid_emails_cn.csv', 'wb')
f_invalid = open('invalid_emails_cn.csv', 'wb')

for email in emails:
    domain = email.split('@')[1]
    if domain in invalid_domains:
        print >>f_invalid, email
    else:
        print >>f_valid, email
