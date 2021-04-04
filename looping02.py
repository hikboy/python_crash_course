favorite_lang = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

for name in sorted(favorite_lang.keys()):
	print(f"{name.title()}, thank you")

print("The following lang have been mentioned:")

for lang in favorite_lang.values():
	print(f"{lang.title()}")


print("- Below use set -")

for lang in set(favorite_lang.values()):
	print(f"{lang.title()}")