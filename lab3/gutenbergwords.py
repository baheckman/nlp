'''
	This program displays text from Gutenberg files.
	To change the file, change the number in the variable "fileno"
	The program gets the raw text, tokenizes and lowercases the tokens.
	It puts the tokens in a frequency distribution and displays the 30 most frequent.
'''
import nltk
from nltk import FreqDist

# change the fileno to give the book that you picked, a number from 0 to 17
fileno = 17

nfile = nltk.corpus.gutenberg.fileids( ) [fileno]
ntext = nltk.corpus.gutenberg.raw(nfile)
print ('First 200 characters of text: ', ntext[:200])
print ()

ntokens = nltk.word_tokenize(ntext)
print ('First 200 tokens: ', ntokens[:200])
print ()

nwords = [w.lower( ) for w in ntokens]

ndist = FreqDist(nwords)

print ('30 Top Frequency Tokens:')
nitems = ndist.most_common(30)
for item in nitems:
    print (item[0], item[1])
