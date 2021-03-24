def pluralNoun(word):
    '''
    This function takes a singular English noun as an argument
    and returns the plural of the noun.
    '''
    word = word.lower() # makes every input of the word lowercase
    vowelsList = ['a', 'e', 'i', 'o', 'u']

    # church --> churches, bush --> bushes, fox --> foxes
    if word.endswith(('ch', 's', 'sh', 'x','z')):
        plural = word + 'es'
    # potato --> potatoes
    elif word.endswith('o') and word[-2] not in vowelsList:
        plural = word + 'es'
    # city --> cities
    elif word.endswith('y') and word[-2] not in vowelsList:
        plural = word.replace('y', 'ies')
    # woman --> women
    elif word.endswith('man'):
        plural = word.replace('man', 'men')
    # special cases
    elif word == 'goose':
        plural = 'geese'
    elif word == 'ox':
        plural = 'oxen'
    elif word == 'mouse':
        plural = 'mice'
    elif word == 'sheep' or word == 'deer':
        plural = word
    #everything else 
    else:
        plural = word + 's'
    
    return plural

print(pluralNoun('tax'))
      
def singularVerb(word):
    '''
    This function takes an English verb as an argument and returns the
    form of the verb used with a 3rd person singular subject (he, she, it)
    '''
    word = word.lower() # makes every input of the word lowercase
    wordList = word.split() # splits the input words into lists
    singularNouns = ['he', 'she', 'it']
    verb = ''

    # if number of words in list is 1
    if len(wordList) == 1:
        if wordList[0].endswith(('ch', 's', 'sh', 'x','z')):
            verb = wordList[0] + 'es'
        elif wordList[0].endswith('o') and wordList[0][-2] not in 'aeiou':
            verb = wordList[0] + 'es'
        elif wordList[0].endswith('y') and wordList[0][-2] not in 'aeiou':
            verb = wordList[0].replace('y', 'ies')
        elif wordList[0] == 'have':
            verb = 'has'
        elif wordList[0] == 'are':
            verb = 'is'
        else:
            verb = wordList[0] + 's'
            
    # if number of words in list is 2
    if len(wordList) == 2:
        # they tax --> they tax, they eat --> they eat
        if wordList[0] == 'they':
            verb = ' '.join(wordList)
        # bob tax --> bob taxes
        elif wordList[0] not in singularNouns and wordList[1].endswith(('ch', 's', 'sh', 'x','z')):
            verb = wordList[0]+' '+wordList[1]+'es'
        # she eat --> she eats
        elif wordList[0] in singularNouns and not wordList[1].endswith(('ch', 's', 'sh', 'x','z')):
            verb = wordList[0]+' '+ wordList[1]+'s'
        else:
            verb = wordList[0]+' '+wordList[1]+'s'
    
    return verb

'''
if __name__ == '__main__':
  nounTests = (
    ('dog','dogs'),
    ('tax','taxes'),
    ('ox','oxen'),
    (city, cities),
    (goose, geese),
    (mouse, mice)
    )
  verbTests = (
    ('eat','eats'),
    ('tax','taxes'),
    ('have','has'),
    ('he eat', 'he eats'),
    )
  battery = (('Plural of noun', pluralNoun, nounTests),
             ('Singular of verb', singularVerb, verbTests))
  for msg,func,tests in battery:
    for (s,t) in tests:
      guess = func(s)
      if guess != t:
        print(msg,s,'is incorrect; expected',t,'but got',guess)
'''
