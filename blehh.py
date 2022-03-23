from scripts.spell_check import *
c=[]
corpus=loadCorpus(c)
t=input('enter the text')
words = t.strip().split()
corrected=[]
for word in words:
    if word not in corpus :
        corrected.append(getCorrectWord(word,corpus))
    else:
        corrected.append(word)    
print(' '.join(corrected))