fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File not found', fname)
    quit()
lines = fh.readlines()
for line in lines:
    print(line.upper().rstrip())


