word = input('enter a word: ') 
letters = list(word)
for i in range(len(word)):
    print(''.join(letters[:i+1]))
