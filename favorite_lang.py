favorite_lang = {
	'jen':['python', 'ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}

for name, lang in favorite_lang.items():
print(f"\n{name.title()}'s favorite language are: ")
	for l in lang:
		print(f"{l.title()}")
