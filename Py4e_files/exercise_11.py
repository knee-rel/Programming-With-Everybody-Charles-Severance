import re
filename = input('Enter filename: ')

try:
    open_file = open(filename)
except:
    print('File not found:',filename)
    quit()

num_sum = 0
for line in open_file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        num_sum = num_sum + int(number)

print(num_sum)

