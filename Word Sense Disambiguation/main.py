import utils as ut
import disambiguation as dt
import testsemcor as ts
import nltk
import re
from prettytable import PrettyTable
from nltk.corpus import semcor as sc

sentences = ut.openFile('./txtFiles/sentences.txt')
original_sentences = []
words_to_analyze = []
choosen_synsets = []
new_sentences = []

for s in sentences:

    keyword = s['word']
    phrase = s['sentence']
    best_sense = dt.lesk( phrase, keyword)

    #getting synonyms of the ambiguous word from its disambigued sense
    synonyms = str(best_sense.lemma_names())

    #creating a new sentence replacing the ambiguous word with its synonyms
    new_sentence = phrase.replace(keyword, synonyms )

    #creating the lists of results
    words_to_analyze.append(keyword)
    original_sentences.append(phrase)
    choosen_synsets.append(best_sense.name())
    new_sentences.append(new_sentence)
#creating a table containing the results
results = PrettyTable()
results.add_column("Original Sentences", original_sentences )
results.add_column("Ambiguous Word", words_to_analyze )
results.add_column("Choosen Synset", choosen_synsets)
results.add_column("New Sentence", new_sentences )

#write the table to a file
table_txt = results.get_string()
with open('./output/Output Word Disambiguation.txt','w') as file:
    file.write(table_txt)

#----------------------------------------------------- SEMCOR TESTING -------------------------------------------#

#getting already semantically tagged sentences from semcor corpus
sem_tagged_sentences = sc.tagged_sents(tag = 'sem')[1:50]
#getting the same sentences untagged
semcor_sentences = sc.sents()[1:50]
#getting already pos tagged sentences from semcor corpus
pos_tagged_sentences = sc.tagged_sents(tag = 'pos')[1:50]
semtest_results = ts.semcorDisambiguation(sem_tagged_sentences,semcor_sentences, pos_tagged_sentences)
semtest_sample = semtest_results[0][1:10]
table_txt_semcor = semtest_results[0].get_string()
with open('./output/Output Semcor Testing.txt','w') as file:
    file.write(table_txt_semcor+"\r\n")
    file.write("Accuracy: "+str(semtest_results[1])+"%")
sample_text = semtest_sample[0].get_string()

#Su 50 prove la media di accuratezza è stata del 41,32%
