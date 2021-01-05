import csv

"""
Process the file containing the nasari reference. In my implementation i don't need the weights.
Input:
    nasari_vector: nasari reference in the form [[babelnetid, word1, correlated term1_weight1,...]...]
Output:
    new_vector: list of nasari vectors in the form [[babelnetid, word1, correlated term1,...]...]
"""
def processNasari(nasari_vector):
    new_vector = []
    for l in nasari_vector:
        nasari_line = []
        for e in l:
            stripped = e.split('_', 1)[0]
            nasari_line.append(stripped)
        new_vector.append(nasari_line)
    return new_vector

#importing files section
def importNasari(path):
    results = []
    with open(path, 'r', encoding='utf8') as file:
            for line in file.readlines():
                tokens = line.rstrip().split(";")
                results.append(tokens)
    for n in results:
        n.pop(0)
    return results
#writng results section
def importDocument(path):
    results = []
    with open(path, 'r', encoding='utf8', newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    results = [x for x in results if x != []]
    return results

def writeSummarization(document, filepath):
    #with open(filepath, "w") as outfile:
        #outfile.write("\n".join(str(item) for item in document))
    with open(filepath,"w") as f:
        wr = csv.writer(f)
        wr.writerows(document)

