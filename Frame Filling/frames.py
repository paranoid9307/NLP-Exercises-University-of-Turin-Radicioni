import nltk
from nltk.corpus import framenet as fn 
#call framenet api
def getFrameData(frame_id):
    frame = fn.frame_by_id(frame_id)
    f_name = frame.name
    f_elem = frame.FE
    f_lus = frame.lexUnit
    f_ctx = getFrameContext(frame)
    return f_name, f_elem, f_lus, f_ctx

def getFrameWords(frame_id):
    frame = fn.frame_by_id(frame_id)
    f_name = frame.name
    f_elem = list(frame.FE.keys())
    f_lus = frame.lexUnit
    lus_names_list = []
    lu_keys = f_lus.keys()
    for l in lu_keys:
        lus_names_list.append(f_lus[l].lexemes[0].name) 
    return f_name, f_elem, lus_names_list

def getFrameContext(frame):
    return(bagOfWords(frame.definition))
#method that process a sentence removing stopwords, punctuation and lemmatizing
def bagOfWords(sentence):
    stop_words = set(open('./txtFiles/stop_words_FULL.txt').read().split())
    sentence = sentence.replace("'", " ")
    sentence = sentence.replace("_", " ")
    sentence = sentence.replace("-", " ")
    sentence = sentence.replace("`", " ")
    punct = {',', ';', '.', '(', ')', '{', '}', ':', '?', '!', "''"}
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(sentence)
    tokens = filter(lambda x: x not in stop_words and x not in punct, tokens)
    return set((lemmatizer.lemmatize(w) for w in tokens))

