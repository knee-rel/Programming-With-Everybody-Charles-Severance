name = input('Enter file: ')

try:
    handle = open(name)
except:
    print('File not found:',name)
    quit()

email_dict = dict()
for line in handle:
    if line.startswith('From '):
        email = line.split()[1]
        email_dict[email] = email_dict.get(email, 0) + 1

freq_address = None 
freq_emails = 0   
for user in email_dict:
    if email_dict[user] > freq_emails:
        freq_address = user
        freq_emails = email_dict[user]

print(freq_address, freq_emails)
            


