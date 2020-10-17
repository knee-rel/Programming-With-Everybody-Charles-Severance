filename = input('Enter file name: ')

try:
    open_file = open(filename)
except:
    print('File not found:', filename)
    quit()

hours = {}
for line in open_file:
    if line.startswith('From '):
        time = line.split()[5]
        times = time[0:2]
        hours[times] = hours.get(times, 0) + 1

lst = list(hours.items())
lst.sort()

for count in lst:
    print(count[0],count[1])
        