from nltk import *
textfile = 'Pride and Prejudice.txt'
text = open(textfile)
tagText = pos_tag(word_tokenize(text.read()))
AdjCounter = 0
WordCounter = 0
for word in tagText:
    if word[1].startswith('JJ') or word[1].startswith('RB'):
        AdjCounter += 1
        WordCounter += 1
    else:
        WordCounter += 1
        
print text.name + ' contains ' + str(WordCounter) +' word, ' + str(AdjCounter) +'(' + str(round(AdjCounter/float(WordCounter) * 100, 1)) + '%) of wich are adjectives.'
raw_input('Press enter to exit.')
