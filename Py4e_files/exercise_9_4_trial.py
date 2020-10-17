filename = input('Enter a file name: ')
fhand = open(filename)
email_addresses = dict()

for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1

max_emails = 0
max_address = None
for k in email_addresses:
    if email_addresses[k] > max_emails:
        max_emails = email_addresses[k]
        max_address = k

print(max_address,max_emails)