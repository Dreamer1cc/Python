import random
def answer_robot(c, var):
	if c == 0:
		c = random.randint(1,10)
	elif var == 'Don\'t Guess. Very small number':
		c += 1
	elif var == 'Don\'t Guess. Very big number':
		c -= 1
	return c

def question():
	var = ''
	a = 0
	b = 0
	b = answer_robot(b, var)
	answer = 'yes'
	while answer != 'no':
		a = random.randint(1,10)
		while b != a:
			b = answer_robot(b, var)
			if b < a:
				var = 'Don\'t Guess. Very small number'
				print (var, b)
			elif b > a:
				var = 'Don\'t Guess. Very big number'
				print (var, b)
		else:
			print ('Lucky Robot shit! You are right! IT IS:', b)
			answer = raw_input('Want play once more? Yes\No: ').lower().strip()
	else:
		print ('Game over')

print question()