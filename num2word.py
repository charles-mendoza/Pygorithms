ones = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
tens = [ 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]
teens = [ 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]
place = [ '', 'thousand', 'million', 'billion', 'trillion',
		  'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion',
		  'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion',
		  'quattuordecillion', 'quindecillion', 'sexdecillion', 'sexdecillion', 'septendecillion',
		  'octodecillion', 'novendecillion', 'vigintillion', 'unvigintillion', 'duovigintillion',
		  'tresvigintillion', 'quattuorvigintillion', 'quinquavigintillion', 'sesvigintillion', 'septemvigintillion',
		  'octovigintillion', 'novemvigintillion', 'trigintillion', 'untrigintillion', 'duotrigintillion',
		  'trestrigintillion', 'quattuortrigintillion', 'quinquatrigintillion', 'sestrigintillion', 'septentrigintillion',
		  'octotrigintillion', 'noventrigintillion', 'quadragintillion', 'quinquagintillion', 'sexagintillion',
		  'septuagintillion', 'octogintillion', 'nonagintillion', 'centillion', 'uncentillion',
		  'decicentillion', 'undecicentillion', 'viginticentillion', 'unviginticentillion', 'trigintacentillion',
		  'quadragintacentillion', 'quinquagintacentillion', 'sexagintacentillion', 'septuagintacentillion', 'octogintacentillion',
		  'nonagintacentillion', 'ducentillion', 'trecentillion', 'quadringentillion', 'quingentillion',
		  'sescentillion', 'septingentillion', 'octingentillion', 'nongentillion', 'millinillion']

def to_tens(val):
	v = str(val)
	x = int(v[0])
	ret = ''

	if val < 20:
		tweens = ones + teens
		ret = tweens[val]
	elif val % 10 == 0:
		ret = tens[val//10-1]
	elif val < 100:
		y = int(v[1])
		ret = tens[x-1] + ' ' + ones[y]

	return ret

def to_hundreds(val):
	v = str(val)
	ret = ''

	if val < 100:
		ret = to_tens(val)
	elif val < 1000:
		y = int(v[-2:])
		x = int(v[0:-2])
		ret = to_tens(x) + ' hundred'
		if y != 0:
			ret += ' ' + to_tens(y)

	return ret

def num2word(val):
	ret = ''
	iVal = int(val)
	length = len(val)
	l = length // 3
	if length % 3 == 1 or length % 3 == 2:
		l += 1

	for i in range(l):
		x = int(val[-3:])
		w = to_hundreds(x)
		if l == 1:
			ret = w
		elif w != 'zero':
			ret = w + ' ' + place[i] + ' ' + ret
		val = val[0:-3]

	return ret

val = input("Enter number:")
val = num2word(val)

print(val)