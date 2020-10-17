fname = input('Enter file name: ')
count = 0
email_lst = []
try:
    fh = open(fname)
except:
    print('File not found:',fname)
    quit()
for line in fh:
    if line.startswith('From:'):
        email = line.rstrip().split()
        count += 1
        print(email[1])   
print('There were', count, 'lines in the file with From as the first word')
