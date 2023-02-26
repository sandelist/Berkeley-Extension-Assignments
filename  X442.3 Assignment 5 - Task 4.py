# Task 4 - Reading lines of a file until the 1000 characters, excluding lines starting with '#'

f = open("UN_speech.txt", "r")

text = ""

for x in f:
        
    if x.startswith('#') != True:
        
        print(x)
        text = text + x
    
    if len(text) >= 1000:
        print('We have reached 1,000 or more characters, excluding lines starting with #')
        print('Number of characters counted: ' + str(len(text)))
        break