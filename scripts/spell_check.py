


def loadCorpus(corpus):
    #function to load the dictionary/corpus and store it in a global list
    with open('hindi_corpus.txt',encoding='utf-8') as file:
        a=1
        for word in file:
            word = word.strip()
            corpus.append(word)
    return corpus
def getLevenshteinDistance(s, t):

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(1, rows):
        dist[i][0] = i

    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution

    return dist[row][col]

def getCorrectWord(word,corpus):
    min_dis=100
    correct_word=""
    for s in corpus:
        cur_dis = getLevenshteinDistance(s,word)
        if min_dis > cur_dis :
            min_dis = cur_dis
            correct_word = s
    return correct_word
    

    
"""
if __name__ == "__main__":
    #main function : execution starts from here
    pass"""
    

