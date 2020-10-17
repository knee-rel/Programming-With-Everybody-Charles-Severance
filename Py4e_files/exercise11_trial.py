import re
hand = open('regex_sum_577365.txt', 'r')
num_sum = 0

for line in hand:
    numbers = re.findall('[0-9]+',line)
    for number in numbers:
        num_sum += int(number)

print(num_sum)