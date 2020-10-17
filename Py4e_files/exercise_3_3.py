score = input('Enter Score: ')
float_score = float(score)

if float_score < 1.0 and float_score > 0.0:
    if float_score < 0.6 and float_score > 0.0:
        print('F')
    elif float_score >= 0.6 and float_score < 0.7:
        print('D')
    elif float_score >= 0.7 and float_score < 0.8:
        print('C')
    elif float_score >= 0.8 and float_score < 0.9:
        print('B')
    elif float_score >= 0.9 and float_score <= 1.0:
        print('A')
else:
    print('Please enter a number within 0.0 and 1.0 to get a grade.')
    quit()
