
alien_0 = {}

alien_0['color'] = 'green'
alien_0['high'] = 15

print(alien_0)

print(f"The alien if {alien_0['high']}")

alien_0['x_pos'] = 5
alien_0['y_pos'] = 15

print(alien_0)

alien_0['speed'] = 'medium'


if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

print(x_increment)

alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print(f"new postion: {alien_0['x_pos']}")

print(alien_0)

del alien_0['y_pos']

print(alien_0)