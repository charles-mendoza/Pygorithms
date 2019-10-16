roman = [
	[ 'N', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX' ], # ones
	[ 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC' ], # tens
	[ 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM' ], # hundreds
	[ 'M', 'MM', 'MMM', '(IV)', '(V)', '(VI)', '(VII)', '(VIII)', '(IX)' ] # thousands
]

def to_tens(val):
	v = str(val)
	ret = ''

	if val < 10:
		ret = roman[0][val]
	elif val % 10 == 0:
		ret = roman[1][val//10-1]
	elif val < 20:
		ret = roman[1][0] + roman[0][int(v[1])]
	elif val < 100:
		ret = roman[1][int(v[0])-1] + roman[0][int(v[1])]

	return ret

def to_hundreds(val):
	v = str(val)
	ret = ''

	if val < 100:
		ret = to_tens(val)
	elif val < 1000:
		x = int(v[0:-2])
		y = int(v[-2:])
		ret = roman[2][x-1]
		if y != 0:
			ret += to_tens(y)

	return ret

def to_thousands(val):
	v = str(val)
	ret = ''

	if val < 1000:
		ret = to_hundreds(val)
	elif val < 10000:
		x = int(v[0:-3])
		y = int(v[-3:])
		ret = roman[3][x-1]
		if y != 0:
			ret += ' ' + to_hundreds(y)

	return ret

def num2roman(val):
	ret = ''
	iVal = int(val)

	if iVal < 10000:
		return to_thousands(iVal)

	length = len(val)
	places = length // 3
	if length % 3 != 0:
		places += 1

	for i in range(places):
		x = int(val[-3:])
		w = to_hundreds(x)
		for j in range(i):
			w = '(' + w + ')'
		if w != 'N':
			ret = w + ' ' + ret
		val = val[0:-3]

	return ret

val = input("Enter number: ")
val = num2roman(val)

print(val)
