def make_pizza(size, *toppings):
	"""Print the list of toppings that have been requested."""
	print(f"make {size} inch pizza")
	for topping in toppings:
		print(topping)
	print('game over')

make_pizza(12, 'pepperoni')
make_pizza(17, 'mushrooms', 'green peppers', 'extra cheese')