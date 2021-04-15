responses = {}

polling_active = True

while polling_active:
	name = input("\n Your name: ")
	response = input("Mountain you like to climb: ")

	responses[name]=response

	repeat = input("Would you like to input another person? yes/no")

	if repeat == 'yes':
		continue
	else:
		break

print("\n Poll results")

for name, response in responses.items():
	print(f"{name} would like to climb {response}")


