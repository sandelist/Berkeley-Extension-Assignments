# Task 1 

def read_text(file_name):
    
    f = open(file_name, "r")


    lines = 0
    words = 0
    characters = 0

    text = ""

    for i in f.readlines():
        lines += 1
        words += len(i.split())
        characters += len(i)

    numbers = (lines, words, characters)
    
    print(numbers)
    return numbers

# Suppose we use the function to read a speech by Rishi Sunak: 

read_text("Sunak_speech.txt")
