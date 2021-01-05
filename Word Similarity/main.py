import nltk
import scipy
import utils as ut
import metrics as me
from nltk.corpus import wordnet as wn
from nltk.corpus import semcor
from prettytable import PrettyTable
from scipy.stats import pearsonr, spearmanr

#loading the couples of word to calculate similarity between them
couples = ut.load_csv('./csvFiles/WordSim353.csv')

#creating the list that will contain the results
term1 = []
term2 = []
target = []
wup_Distance = []
sp_Distance = []
lc_Distance = []

#calculate the similarity using three different metrics
for r in couples[:]:
    #getting wordnet synsets of the given words
    synset1 = wn.synsets(r[0])
    synset2 = wn.synsets(r[1])

    term1.append(r[0])
    term2.append(r[1])
    target.append(r[2])
    
    #calculate the three different similarity metrics
    wup_Distance.append(me.wupSimilarity(synset1, synset2))
    sp_Distance.append(me.shortestPathSimilarity(synset1, synset2))
    lc_Distance.append(me.leakChodSimilarity(synset1, synset2))

#creating a table containing the two words to confront, the human annotated similarity 
#and the three different similarities found by the algorithm
results = PrettyTable()
results.add_column("First term",term1 )
results.add_column("Second term",term2 )
results.add_column("Target",target )
results.add_column("Wup Distance",wup_Distance )
results.add_column("Shortest Path Distance",sp_Distance)
results.add_column("Leakcock & Chod Distance",lc_Distance)

#writing the table on a file
ut.writeTable(results,'./output/termSimilarities.txt')

#------------------------------------------------ CORRELATION ---------------------------------------------#
#calculating the correlation between the human annotated similarities score and the ones
#given by the algorithm, using the Pearson correlation measure and the Spearmann correlation measure

#Pearson correlation
wup_pcorr, _ = pearsonr(wup_Distance, target)
sp_pcorr, _ = pearsonr(sp_Distance, target)
lc_pcorr, _ = pearsonr(lc_Distance, target)

#Spearmann correlation
wup_scorr, _ = spearmanr(wup_Distance, target)
sp_scorr, _ = spearmanr(sp_Distance, target)
lc_scorr, _ = spearmanr(lc_Distance, target)

#creating a table that contain the correlation values
correlation = PrettyTable()
correlation.field_names = ["Similarity metrics", "Pearson correlation", "Spearman correlation"]
correlation.add_row(["Wu&Palmer", wup_pcorr, wup_scorr])
correlation.add_row(["Shortest Path", sp_pcorr, sp_scorr])
correlation.add_row(["Leackock&Chodorow", lc_pcorr, lc_scorr])

#writing the table ton a file
ut.writeTable(correlation,'./output/correlations.txt')


