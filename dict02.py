test = {'color': 'green', 'high': 15, 'x_pos': 7, 'y_pos': 15, 'speed': 'medium'}

#print(test['hello'])

val = test.get('hello', 'no such key found')
print(val)