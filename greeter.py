prompt = "if you tell us who you are"
prompt += "\nWhat is you name?"

name = input(prompt)

age = input("How old are you: ")

age = int(age)

if(age > 18):
	print("older than 18")
else:
	print("younger than 18")
