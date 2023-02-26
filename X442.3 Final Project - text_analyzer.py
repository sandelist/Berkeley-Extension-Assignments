print('Thanks for using our text analyzer!')

quit = False

while quit == False:
    
    textfile = input('Enter text file name without the extension .txt. To quit, enter Q')
    
    if textfile == 'Q':
        quit = True
        print('Thanks for using the text analyzer! See you!')
        
        break
    
    try:
        with open(textfile + '.txt', 'r') as f:
            text_analyzer(textfile)

    except FileNotFoundError:
        print('Text file not found. Please enter another file name')


    def text_analyzer(textfile):

        with open(textfile + '.txt', 'r') as file:
                text = file.read()

        # Convert text to lowercase
        text = text.lower()

        # Count the frequency of words 
        words = text.split()
        counts = {}

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        # Find the number of times the top 5 words are used and sort them by most frequently used count

        top_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
        print('')
        print('Top 5 most frequently used words :')
        for word, count in top_words:
            print(f"{word}: {count}")
        print()

        # Find the longest word in the document

        longest_word = max(words, key=len)
        print('The longest word: ', longest_word)
        print()

        # FInd the average word size

        total_length = sum(len(word) for word in words)
        average_length = total_length / len(words)
        print('The average word size: ', average_length)
        print('')

