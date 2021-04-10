pizza = {
	'crust' : 'thick',
	'toppings':['mushroms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza"
	" this is the second print: ")

for topping in pizza['toppings']:
	print("\t" + topping)