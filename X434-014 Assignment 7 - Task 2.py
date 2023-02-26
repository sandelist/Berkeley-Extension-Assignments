# Task 2 

# Handling KeyboardInterrupt

text = []

try:    
    while True:
        user_input = input('Please type something!')    
        text.append(user_input)
        print(text)

except KeyboardInterrupt:
    print('\nYou pressed your keyboard to stop the programme')
    print('You have exited the programme')