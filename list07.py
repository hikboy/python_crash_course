
digits = list(range(1,200000))

#print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value **2 for value in range(1,11)]
print(squares)
print(squares[0:3])
print(squares[:3])
print(squares[2:])
print(squares[-2:])

for num in squares[-2:]:
	print(num)