text = "X-DSPAM-Confidence:    0.8475"

retrieve = text.find('0.8475')
num = text[retrieve:]
fnum = float(num)
print(fnum)