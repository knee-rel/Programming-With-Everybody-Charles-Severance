def computepay(h,r):
    if h <= 40:
        return (h * r)
    else:
        return (h * r) + (h - 40) * 0.5 * r

hrs = input('Enter Hours: ')
h = float(hrs)
rate = input('Enter Rate: ')
r = float(rate)
p = computepay(h, r)
print('Pay:',p)