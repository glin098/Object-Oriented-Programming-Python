wordsUsed = []
word = input('Start entering words: ')
while word not in wordsUsed:
    if word:
        wordsUsed.append(word)
        word = input('Start entering words: ')
    elif word in wordsUsed:
            print('You alreasy entered', word)
print('You listed', len(wordsUsed),'distinct words')
        
