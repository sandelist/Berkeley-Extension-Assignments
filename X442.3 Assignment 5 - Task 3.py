# Task 3 - Reading lines of a file until the 1000 characters

f = open("UN_speech.txt", "r")

text = ""

for x in f:
    
    print(x)
    
    text = text + x
    
    if len(text) >= 1000:
        print('We have reached 1,000 or more characters')
        print('Number of characters counted: ' + str(len(text)))
        break