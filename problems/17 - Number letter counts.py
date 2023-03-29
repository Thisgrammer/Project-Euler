'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''


w1_9 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
w10_19 =  ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
w20_100 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
w100 = ['hundred']

sumW = 0


sumW += len(w1_9) * 90
sumW += len('hundred') * 900
sumW += len(w10_19) * 90
sumW += len(w20_100) * 90

print(sumW)