# Task 4


def read_list_for_dict(*lists):
    
    count_dict = {}
    
    for i in lists:
        for j in i: 
            if j not in count_dict:
                count_dict[j] = 1
            
            else:
                count_dict[j] = count_dict[j] + 1

    print(count_dict)
    return count_dict


# Suppose we use the three lists given in the questions 

wl1 = ["double", "triple", "int", "quadruple"]
wl2 = ["double", "home run"]
wl3 = ["int", "double", "float"]

read_list_for_dict(wl1,wl2,wl3)
