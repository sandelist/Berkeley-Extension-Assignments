# Task 5


def combining_dicts(*args, **dicts): 
    
    combine_dict = {}

    for i in args:
        
        for j in i:

            if j not in combine_dict:
                combine_dict[j] = i[j]
                
            else:
                
                if isinstance(combine_dict[j], str) == True:
                    combine_dict[j] = [combine_dict[j], i[j]]
                    
                else:
                    
                    if i[j] not in combine_dict[j]:
                        combine_dict[j].append(i[j])                    

    print(combine_dict)
    return combine_dict



# Suppose we use these three dictionaries, and want to combine them into a dictionary which shows key cities in Asia:


asian_capitals = {'Japan':'Tokyo', 
                  'Korea':'Seoul', 
                  'China':'Beijing', 
                  'Malaysia': 'Kuala Lumpur',
                  'India':'New Delhi',
                  'Thailand':'Bangkok'}

big_asian_city_by_GDP = {'China':'Shanghai',
                          'Japan':'Osaka',
                         'Thailand':'Bangkok',
                         'India':'Mumbai',
                         'Singapore':'Singapore',
                         'Malaysia':'Kuala Lumpur'}


big_asian_city_by_population = {'China':'Shanghai',
                          'Japan':'Tokyo',
                         'Indonesia':'Jakarta',
                         'Iran':'Tehran',
                        'India':'Kolkata'}

combining_dicts(asian_capitals, big_asian_city_by_GDP, big_asian_city_by_population)
