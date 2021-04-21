
def print_models(unprinted_designs, completed_mpdels):
	"""
	Simulat printing each design, until none are left.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"printing model: {current_design.title()}") 
		completed_mpdels.append(current_design)

def show_completed_models(completed_mpdels):
	"""
	Show all the models that were printed.
	"""
	print("\nThe following models have been printed")
	for completed_mpdel in completed_mpdels:
		print(completed_mpdel)



unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_mpdels = []

print_models(unprinted_designs[:], completed_mpdels)
print_models(unprinted_designs, completed_mpdels)
show_completed_models(completed_mpdels)