"""from scripts.spell_check import *
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
print(' '.join(corrected))"""

"""from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['caar','hte'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))"""

from spello.model import SpellCorrectionModel  
sp = SpellCorrectionModel(language='en')    
sp.load('model/en.pkl')  
res=sp.spell_correct('i want to plai kricket')  
print(res['spell_corrected_text'])