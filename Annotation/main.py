import utils as ut
import similarity as sim

#creating tsv files from annotations
couples_assign = ut.importTxt('./txtFiles/Assignation.txt')
ut.writePersonalSimilarity(couples_assign)
sense_identification = ut.importTxt('./txtFiles/SenseIdentification.txt')
ut.writeSenseId(sense_identification)

#calculate max cosine similarity between embedded nasari vectors
sense_to_synsets = ut.importWordToId('./txtFiles/SemEval17_IT_senses2synsets.txt')
nasari_vectors = ut.importTsv('./tsvFiles/mini_NASARI.tsv')
max_similarities, best_senses = sim.confrontResults(sense_to_synsets,couples_assign,nasari_vectors)

#calculate Pearson and Spearmann correlation
pearson_corr, spearman_corr = sim.calculateCorrelation(max_similarities, couples_assign)
personal = ut.importTsv('./tsvFiles/personalIdentification.tsv')[1:]

#get results
table, percentage = ut.getTableResult(personal, best_senses)

#writing results on file
table_txt = table.get_string()
with open("./results/results.txt", "a") as a_file:
  a_file.write("The Pearson correlation in my work is equal to: "+str(pearson_corr))
  a_file.write("\n")
  a_file.write("The Spearman correlation in my work is equal to: "+str(spearman_corr))
  a_file.write("\n")
  a_file.write("The percentage of same Babelnet synset ids in my work is equal to: "+str(percentage)+" %")
  a_file.write("\n")
  a_file.write("\n")
  a_file.write(table_txt)



