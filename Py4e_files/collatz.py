def collatz_func(num):
    if num % 2 == 0:
        return num / 2
    else:
        return num * 3 + 1

count = 0
try:
    num_input = input('Enter number: ')
    num = float(num_input)
    while num != 1:
        print(count,'     ',num)
        count = count + 1
        num = collatz_func(num)
except:
    print('Type a number please!')



