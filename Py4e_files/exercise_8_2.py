fname = input('Enter file name: ')
lst = []
try:
    fh = open(fname)
except:
    print('File not found:',fname)
    quit()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
            continue
        else:
            pass
lst.sort()
print(lst)

    

    
