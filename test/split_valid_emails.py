import csv
import os
import shutil


with open('valid_emails.csv', 'rb') as f:
    reader = csv.reader(f)
    emails = map(lambda x:x[0], list(reader))

if os.path.exists('valid'):
    shutil.rmtree('valid')

os.makedirs('valid')
chunks=[emails[x:x+100] for x in xrange(0, len(emails), 250)]

for idx, emails in enumerate(chunks):
    print(idx)
    f_valid = open('valid/valid_emails_' + str(idx+1) + '.csv', 'wb')
    for email in emails:
        print >>f_valid, email

