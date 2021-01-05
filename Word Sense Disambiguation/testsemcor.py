import nltk
import re
import random
import disambiguation as dt
from nltk.corpus import semcor as sc
from prettytable import PrettyTable

#get only the lemmas from the semantic trees in semcor corpus that are in the form (word.n.xx)
def lemmaSemanticList(sent):
    lemma = []
    for l in sent:
        if isinstance(l, nltk.tree.Tree):
            if (isinstance(l.label(),nltk.corpus.reader.wordnet.Lemma)):
               lemma.append((l.label().synset().name()))
            elif (isinstance(l.label(), str)):
                lemma.append((l.label()))
        else:
            lemma.append(None)
    lemma =[w for w in lemma if w]
    return lemma

#get the word in the sentence that are nouns
def getNouns(tagged_sentence):
    nouns = [po.leaves() for po in tagged_sentence 
    if ((po.label() == 'NN' 
    or po.label() == 'NNPS' 
    or po.label() == 'NNS' ) 
    and (len(po.leaves()) == 1))]
    nouns = [val for sublist in nouns for val in sublist]
    return  nouns

#find the sense annotated in semcor for the choosen ambiguous word, using the regular expression search ('word.n.xx)
def getSemcorSense(word, sem_sentence):
    r1 = None
    for s in sem_sentence:
        r1 = re.findall(rf"{word}.\w.\d+", s, re.IGNORECASE)
        if r1: return r1
    return r1

"""
Method that disambiguate a random word from every of the first 50 sentences of the semcor corpus and confront
the choice with the already annotated sense 
Input:
    sem_tagged_sentences: first 50 semcor corpus sentences semantically annotated
    semcor_sentences: first 50 semcor corpus sentences 
    pos_tagged_sentences: first 50 semcor corpus sentences sintattically annotated
Output:
    results: a table containing the sentences analyze, the choosen senses and the annotated ones
    accuracy: a percentage of equal synsets between the automatic and the manual method 
"""

def semcorDisambiguation(sem_tagged_sentences, semcor_sentences, pos_tagged_sentences):
    lemmatizer = nltk.WordNetLemmatizer()
    accuracy = 0
    results = PrettyTable()
    results.field_names = ["Sentence", "Ambiguous word", "Choosen Synset", "Semcor Synset"]

    for i in range(len(semcor_sentences)):
        nouns = getNouns(pos_tagged_sentences[i])
        sentence_to_analyze = " ".join(semcor_sentences[i])
        word_to_analyze = lemmatizer.lemmatize(random.choices(nouns)[0])
        # word_to_analyze = lemmatizer.lemmatize(word_to_analyze)
        best_sense = dt.lesk(sentence_to_analyze, word_to_analyze)
        if not best_sense:
            best_sense = "Not found"
        else:
            best_sense = best_sense.name()
        lemmas = lemmaSemanticList(sem_tagged_sentences[i])
        semcor_sense = getSemcorSense(word_to_analyze, lemmas)
        if not semcor_sense:
            results.add_row([sentence_to_analyze, word_to_analyze, best_sense, lemmas])
        else:
            results.add_row([sentence_to_analyze, word_to_analyze, best_sense, semcor_sense[0]])
            if semcor_sense[0] == best_sense : accuracy+=1
    
    accuracy = (accuracy/50)*100
    return [results, accuracy]
    
    










