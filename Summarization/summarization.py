import nltk

"""
Summarize the document with regards to the given percentage that we want to remove
Input:
    document: the document we want to summarize in the form [[title],[paragraph1],...[paragraphn]]
    nasari: the file containing Nasari vector correlated with words
    percentage: the percentage of the document that we want to remove
Output:
    summ: the document summarized (with a certain number of paragraphs removed)
"""
def summarize(document, nasari, percentage):
    title = getTitle(document)
    titleNasari = []
    paragraphEval = []
    num_rows_to_remove = int((len(document)/100)*percentage)
    index = 0
    for w in title:
        titleNasari.append(findNasari(w, nasari))
    titleNasari = [x for x in titleNasari if x is not None]
    for paragraph in document:
        processed_parag = process(paragraph) 
        WO_value = calculateWO(processed_parag, titleNasari, nasari)
        paragraphEval.append((index, WO_value))
        index+=1
    paragraphEval.sort(key=lambda tup: tup[1], reverse=True)
    summ_indexes =  paragraphEval[:-num_rows_to_remove]
    summ_indexes = [x[0] for x in summ_indexes]
    summ_indexes.sort()
    summ = [document[x] for x in summ_indexes]
    return (summ)

#we get the processed title
def getTitle(document):
    return(process(document[0]))

#Processing the sentence in input, removing the stop words and lemmatizing
def process(sentence):
    sentence = ''.join(sentence)
    stop_words = set(open('./txtFiles/stop_words_FULL.txt').read().split())
    punct = {',', ';', '.', '(', ')', '{', '}', ':', '?', '!', "''"}
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(sentence)
    tokens = filter(lambda x: x not in stop_words and x not in punct, tokens)
    return list((lemmatizer.lemmatize(w) for w in tokens))

#find the nasari vector of the word in input
def findNasari(word, nasari):
    for nasari_vector in nasari:
        if nasari_vector[0].lower() == word.lower():
            return nasari_vector[1:]
    return None

"""
Allow to calculate the Semantic similarity. Implementation of Weight Overlap (Pilehvar et al.)
Input:
    topic: Nasari vector (topic)
    paragraph: Nasari vector (paragraph)
    nasari: the complete file containing Nasari vectors
Output:
    wo_score: the entire paragraph similarity with the topic calculated with Weight overlap
"""
def calculateWO(paragraph, topic, nasari):
    wo_score= 0
    for word in paragraph:
        nasari_word = findNasari(word, nasari)
        if not nasari_word : continue
        for vector in topic:
            commons = list(set(nasari_word).intersection(vector))
            score = 0
            if (len(commons)>0):
                n = sum(1 / (vector.index(q)+1) + (nasari_word.index(q)+1) for q in commons)
                d = sum(list(map(lambda x: 1 / (2 * x), list(range(1, len(commons) + 1)))))
                score = n/d
            #if there's no commons words the score is 0
            wo_score += score
    return wo_score


