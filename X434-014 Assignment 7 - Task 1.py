# Task 1 

# Solving the problem using a try/except clause

user_input = input('Please type something!')

try:
    user_input_number = float(user_input)
    print('Converted number: ', user_input_number )
    
except ValueError:
    print('The text you inputted cannot be converted to number')
    
# Solving the problem using a try/except clause

txt = input('Please type something!')

new_txt = txt.replace('.','')

new_txt = new_txt.replace('-','')

if new_txt.isnumeric() is False:
    print('The text you inputted cannot be converted to number')

elif txt.count('.') > 1:
    print('The text you inputted cannot be converted to number')

elif txt.count('-') > 1: 
    print('The text you inputted cannot be converted to number')
    
else:
    if '-' in txt:
        if txt.rfind('-') == 0:
            user_input_number = float(txt)
            print('Converted number: ', user_input_number )
        else:
            print('The text you inputted cannot be converted to number')
    else:
        user_input_number = float(txt)
        print('Converted number: ', user_input_number )