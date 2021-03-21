first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

mymessage = f"Hello, {full_name.title()}!"
print(mymessage.upper())

# old style
full_old = "{} {}".format(first_name, last_name)
print(full_old)

print("python")
#print(python)
print("\tpython")

favorite_lang = "python "
fdd = "pt"
tt = favorite_lang + fdd
print(tt)

favorite_lang = "python "
fdd = "pt"
tt = favorite_lang.rstrip() + fdd
print(tt)

#lstrip(), strip, rstrip()


