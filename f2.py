
def describe_pet(pet_name, animal_type="cat"):
	print(f"\nI have a {animal_type}")
	print(f"My {pet_name}'s naem is {pet_name.title()}.")
	"""Display information about a pet."""

describe_pet("bird", "hibirdd")
describe_pet("dog", "linda")
describe_pet(pet_name="linda", animal_type="dog")
describe_pet(pet_name="miaomiao")