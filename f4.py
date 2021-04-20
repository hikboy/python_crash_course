def build_person(first_name, last_name, age=None):
	"""Return dict"""

	person = {'first':first_name, 'last':last_name}
	if age:
		person['age'] = age
	return person

laogao = build_person('liu', 'meili')
print(laogao)

laogao1 = build_person('liu', 'meili', 27)
print(laogao1)

while True:
	print("\nPlease input a person: ")
	f_name = input("First name: ")
	l_name = input("Last name: ")

	per = build_person(f_name, l_name)
	print(f"\nHello {per}")