fname = input("Enter file name: ")
count = 0
total_confidence = 0
try:
    fh = open(fname)
except:
    print('File not found:',fname)
    quit()
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"): 
        snum = line.rstrip().split()[1]
        fnum = float(snum) 
        total_confidence += fnum
        count += 1
   
print("Average spam confidence:", total_confidence/count)