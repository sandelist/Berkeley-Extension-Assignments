# Task 1 - Writing a for loop printing the keys and values in the alphabetical order of the keys.

capitals = {'UK':'London','France':'Paris','Germany':'Berlin','Netherlands':'Amsterdam','Spain':'Mardid','Portugal':'Lisbon','Italy':'Rome'}

for i in sorted(capitals.keys()):
    print(i + ' - ' + str(capitals[i]))