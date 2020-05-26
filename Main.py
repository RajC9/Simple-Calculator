number_one=int(input('please enter the first number'))
operator=input('please enter the operator:')
number_two= int(input('please enter the second number'))

if operator == '+':
	print('{}+{}= '.format(number_one,number_two))
	print(number_one+number_two)
elif operator == '-':
	print('{}-{}='.format(number_one,number_two))
	print(number_one-number_two)
elif operator == '*':
	print('{}*{}='.format(number_one,number_two))
	print(number_one*number_two)
elif operator== '/':
	print('{}/{}='.format(number_one,number_two))
	print(number_one/number_two)
else:
	print('invalid')
