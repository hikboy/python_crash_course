favorite_lang = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

friends = ['phil', 'sarah']

for name in favorite_lang.keys():
	print(name.title())

	if name in friends:
		language = favorite_lang[name].title()
		print(f"{name} favorite_lang is {language}")

if 'ljb' not in favorite_lang.keys():
	print(f"ljb , poll please")

