def sum_digits(l):
	r = l % 10
	total = r
	while l / 10 > 0:
		l = l // 10
		r = l % 10
		total += r

	return str(total)

print ('Sum of Digits: '+sum_digits(1234))

def smallest(l):
	small = l[0]
	for i in l:
		if i < small:
			small = i

	return str(small)

#print ('Smallest Digit: '+smallest([10,8,45,2,1,6,9]))

def palindrome(string):
	
	if len(string) > 1:
		if string[0] == string[-1]:
			return palindrome(string[1:-1])
		else:
			return " is not palindrome"
	else:
		return (" is palindrome") 
s = 'madam'
#print (s+palindrome(s))