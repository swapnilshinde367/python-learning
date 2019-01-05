# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# for pair in zip( names, heros ) :
# 	print( pair )

# Usual way
# new_dictionary = {}
# for name, hero in zip( names, heros ) :
# 	new_dictionary[name] = hero
# print(new_dictionary)

#Comprehension
new_dictionary = {name:hero for name,hero in zip( names, heros )}
print(new_dictionary)

# If name is not Peter and Bruce
new_dictionary = {name:hero for name,hero in zip( names, heros ) if name not in ['Peter', 'Bruce']}
print(new_dictionary)

