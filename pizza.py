pizza_size = input( ''' 
How big do you want your pizza?
Type "large" if you want a
large pizza.
Type "extra large" if you want an extra large pizza.
''')

if pizza_size == 'large' or pizza_size == 'extra large':
	toppings = int(input( 'State how many toppings you would like. You have the option between 1 to 4: '))
	if pizza_size == 'large':
		if toppings == 1:
			subtotal = 6 + 1 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 2:
			subtotal = 6 + 1.75 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 3:
			subtotal = 6 + 2.50 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total), 2)	)
		elif toppings == 4:
			subtotal = 6 + 3.35 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		else:
		    print('Invalid number of toppings. Please restart and choose a number of toppings you wish between 1 and 4.')
	elif pizza_size == 'extra large':
		if toppings == 1:
			subtotal = 10 + 1 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 2:
			subtotal = 10 + 1.75 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 3:
			subtotal = 10 + 2.50 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total), 2)	)
		elif toppings == 4:
			subtotal = 10 + 3.35 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		else:
		    print('Invalid number of toppings. Please restart and choose a number of toppings you wish between 1 and 4.')
	else:
		print( 'Invalid size. Please pick between "large" or "extra large".')
else: 
	print( 'Invalid size. Please pick between "large" or "extra large".')


input('You have ordered your pizza. Please come again.')
