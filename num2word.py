ones = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
tens = [ 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]
teens = [ 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]
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
	ret = ''

	if val < 10:
		ret = ones[val]
	elif val % 10 == 0:
		ret = tens[val//10-1]
	elif val < 20:
		ret = teens[int(v[1])-1]
	elif val < 100:
		ret = tens[int(v[0])-1] + ' ' + ones[int(v[1])]

	return ret

def to_hundreds(val):
	v = str(val)
	ret = ''

	if val < 100:
		ret = to_tens(val)
	elif val < 1000:
		x = int(v[0:-2])
		y = int(v[-2:])
		ret = to_tens(x) + ' hundred'
		if y != 0:
			ret += ' ' + to_tens(y)

	return ret

def num2word(val):
	ret = ''
	iVal = int(val)
	length = len(val)
	places = length // 3
	if length % 3 != 0:
		places += 1

	for i in range(places):
		x = int(val[-3:])
		w = to_hundreds(x)
		if places == 1:
			ret = w
		elif w != 'zero':
			ret = w + ' ' + place[i] + ' ' + ret
		val = val[0:-3]

	return ret

val = input("Enter number: ")
val = num2word(val)

print(val)
