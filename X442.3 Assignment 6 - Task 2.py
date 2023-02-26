# Task 2

# Suppose the function takes 4 lists


def read_list(list_1, list_2, list_3, list_4):
    
    list_output = []
    
    for i in [list_1, list_2, list_3, list_4]:
        for j in i:
            list_output.append(j)
    
    print(list(set(list_output)))
        
    return list(set(list_output))

# Suppose we use the function to handle four lists: 
# ['a','b'],['c','d'],['e','f'],['a','e','y']

read_list(['a','b'],['c','d'],['e','f'],['a','e','y'])
