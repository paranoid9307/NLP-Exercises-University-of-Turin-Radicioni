import csv
from prettytable import PrettyTable

#Importing files section
def importTsv(path):
    list_r= []
    with open(path,"r", encoding='latin-1') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            list_r.append(line)
    list_r = [s for s in list_r if len(s)>0]
    return list_r

def importTxt(path):
    results = []
    with open(path,"r", encoding='utf-8') as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
    return results
#The difference between the precedent method is that I use the extend function
#instead of append function, because I need a flat list
def importSenseTxt(path):
    results = []
    with open(path, "r", encoding='utf-8' ) as inputfile:
        for line in inputfile:
            results.extend(line.strip().split('\t'))
    return results
#Method that is used to create the list in the form [[word1, [babelnet ids]],...[wordn, [babelnet ids]]]
def importWordToId(path):
    results = importSenseTxt(path)
    word_babelsynset = []
    word = []
    synsets = []
    for e in results:
        if '#' in e:
            word.append(synsets)
            word_babelsynset.append(word)
            e = e.replace('#', "")
            word = []
            synsets = []
            word.append(e)
        else:
            synsets.append(e)
    return word_babelsynset
#this is the "write on external files" section, used to create the tsv files 
# containing personal annotation
def writePersonalSimilarity(personal_annotation):
    with open('./tsvFiles/personalAnnotation.tsv', 'wt', newline='') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(['Term1', 'Term2', 'Similarity'])
        for l in personal_annotation:
            tsv_writer.writerow(l)

def writeSenseId(sense_identification):
    with open('./tsvFiles/personalIdentification.tsv', 'wt', newline='') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(['Term1', 'Term2', 'Id1', 'Id2', 'Synonyms1', 'Synonyms2'])
        for l in sense_identification:
            if len(l)>0:
                lst = [x for y in l for x in y.split(';')]
                tsv_writer.writerow(lst)
            else: continue

#the two subsequent methods are used to extract just the babel ids respectively
#from the personal file and the list created automatically
def getPersonalBabelIds(annotation_list):
    babel_ids1=[]
    babel_ids2 = []
    for l in annotation_list:
        babel_ids1.append(l[2])
        babel_ids2.append(l[3])
    return babel_ids1, babel_ids2
def getBabelIds (automatic_annotation):
    babel_ids1=[]
    babel_ids2 = []
    for l in automatic_annotation:
        if l:
            babel_ids1.append(l[0])
            babel_ids2.append(l[1])
        else:
            babel_ids1.append(None)
            babel_ids2.append(None)
    return babel_ids1, babel_ids2
"""
Create the table containing the personal babel ids and the automatic ones and calculate the percentage of 
common ids 
Input:
    personal_identification: a list of babel ids in the form [word1, word2, choosen babel id1, choosen babel id2...]
    automatic_identification: a list of babel ids in the form [babel id1, babel id2]
Output:
    x: the constructed table
    round(percentage,2): the percentage of common ids rounded
"""
def getTableResult(personal_identification,automatic_identification):
    personal_id1, personal_id2 = getPersonalBabelIds(personal_identification)
    automatic_sense1, automatic_sense2 = getBabelIds(automatic_identification)
    total_len = len(personal_id1)+ len(personal_id2)
    count = len([s for s in personal_id1 if s in automatic_sense1])
    count += len([s for s in personal_id2 if s in automatic_sense2])
    percentage = (count/total_len)*100
    x = PrettyTable()
    column_names = ["Personal term 1 synset", "Personal term 2 synset", "Automatic term 1 synset", "Automatic term 2 synset"]
    x.add_column(column_names[0], personal_id1)
    x.add_column(column_names[1], personal_id2)
    x.add_column(column_names[2], automatic_sense1)
    x.add_column(column_names[3], automatic_sense2)
    return x, round(percentage,2)
