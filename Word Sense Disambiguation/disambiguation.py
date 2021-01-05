import nltk
import csv
from nltk.corpus import wordnet as wn

#lesk function as implemented from the nltk team
def lesknltk(context_sentence, ambiguous_word, pos=None, synsets=None):
    context = set(context_sentence)
    if synsets is None:
        synsets = wn.synsets(ambiguous_word)
    if pos:
        synsets = [ss for ss in synsets if str(ss.pos()) == pos]
    if not synsets:
        return None
    _, sense = max((len(context.intersection(ss.definition().split())), ss) for ss in synsets)
    return sense

"""
Allow to get the best sense for a given word
Input:
    context: the sentence in which the ambiguous word is
    keyword: the word we need to disambiguate
Output:
    best_sense: the most probable synset
"""
def lesk(context, keyword):
    synsets = wn.synsets(keyword)
    if not synsets:
        return None
    best_sense = synsets[0]
    max_overlap = 0
    context_words = bagOfWords(context)
    for sense in synsets:
        signature = bagOfWords(sense.definition())
        examples = sense.examples()
        for ex in examples:
            signature.update(bagOfWords(ex))
        overlap = len(signature.intersection(context_words))
        if overlap> max_overlap:
            max_overlap = overlap
            best_sense = sense
    return best_sense
    
#method that process a sentence or a word, removing stopwords, punctuation and lemmatizing
def bagOfWords(sentence):
    stop_words = set(open('./txtFiles/stop_words_FULL.txt').read().split())
    punct = {',', ';', '(', ')', '{', '}', ':', '?', '!'}
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(sentence)
    tokens = filter(lambda x: x not in stop_words and x not in punct, tokens)
    return set((lemmatizer.lemmatize(w) for w in tokens))






