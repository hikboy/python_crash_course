
aliens = []

for alien_num in range(30):
	new_alien = {'color':'green', 'point':5, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

print("...")

print(f"Total number of aliens: {len(aliens)}")


for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'fast'
		alien['point'] = 10

for alien in aliens[:5]:
	print(alien)
