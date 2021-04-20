def get_formatted_naem(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_naem('jb', 'l')
print(musician)

musician1 = get_formatted_naem('hi', 't', 'c')
print(musician1)
