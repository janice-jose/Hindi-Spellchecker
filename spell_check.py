corpus = []

def loadCorpus():
    #function to load the dictionary/corpus and store it in a global list
    with open('hindi_corpus.txt',encoding='utf-8') as file:
        a=1
        for word in file:
            word = word.strip()
            corpus.append(word)

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

def getCorrectWord(word):
    min_dis=100
    correct_word=""
    for s in corpus:
        cur_dis = getLevenshteinDistance(s,word)
        if min_dis > cur_dis :
            min_dis = cur_dis
            correct_word = s
    return correct_word
    
def processInput():
    cur_line_num = 0
    out = open('output.txt', 'w', encoding='utf-8')
    with open('input1.txt',encoding='utf-8') as file:
        for line in file:
            cur_line_num += 1
            cur_word_num = 0
            words = line.strip().split()
            for word in words:
                cur_word_num+=1
                if word not in corpus :
                    corrected= getCorrectWord(word)
                    out.write("At Line:" + str(cur_line_num) + " Word No. "+str(cur_word_num) +" : "+ word + "  -> " + corrected + "\n")
                    out.flush()
    

if __name__ == "__main__":
    #main function : execution starts from here
    loadCorpus()
    processInput()

