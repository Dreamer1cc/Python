#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
a = 0
b = ''
answer = 'yes'
while answer != 'no':
	a = random.randint(1,10)
	while b != a:
		b = raw_input('What is my number? (1-10): ')
		if b.isdigit() == True:
			b = int(b)
			if b < a:
				print ('Don\'t Guess. Very small number')
			elif b > a:
				print ('Don\'t Guess. Very big number')
		else:
			print ('It is not a digit')
	else:
		print ('Lucky Human! You are right!')
		answer = raw_input('Want play once more? Yes\No: ').lower().strip()
else:
	print ('Game over')