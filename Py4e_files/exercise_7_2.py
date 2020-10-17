fname = input("Enter file name: ")
total = 0
average = 0
try:
    fh = open(fname)
except:
    print('File not found:',fname)
    quit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    snum = line.rstrip().split()[1]

        fnum = float(snum)
        break
    print(fnum)
total = fnum + 1
average = total / fnum
print("Average spam confidence: ", total, average)