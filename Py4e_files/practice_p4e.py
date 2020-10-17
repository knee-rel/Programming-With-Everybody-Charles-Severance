x = 0
total = 0.0

while True:
    snum = input('Enter a number: ')

    if snum == 'done':
        break

    try:
        fnum = float(snum)

    except:
        print('Please enter a valid input.')
        continue

    x += 1
    total += fnum
    average = total/x

print(total, x, average)

        
