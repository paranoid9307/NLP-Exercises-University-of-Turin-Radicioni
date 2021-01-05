import utils as ut
import numpy as np
import scipy
from scipy.stats import pearsonr, spearmanr
from numpy.linalg import norm
"""
Calculate similarity score (based on cosine similarity) of a list of couple of terms from Nasari vector.
Input:
   sense_to_synsets: list in the form [[word1,[babelnet ids]],...[wordn, [babelnet ids]]]
   couples_assign: list in the form [[term1, term2, annotated similarity score],
   ...[termn, termn+1, annotated similarity score]]
   nasari_vectors: list of nasari vector
    
Output:
   max_similarities: list of similarity scores between the words in couples_assign
   best_senses: argmax for the cosine similarity between words (the couple
   of senses which maximize the function) 
"""
def confrontResults(sense_to_synsets, couples_assign, nasari_vectors):
    max_similarities = []
    best_senses = []
    for lists in couples_assign:
        id_term1 = findIds(lists[0], sense_to_synsets)
        id_term2 = findIds(lists[1], sense_to_synsets)
        if (not id_term1 or not id_term2):
            max_similarities.append(None)
            best_senses.append(None)
            continue
        max_similarity, indexes = calculateMaxSimilarity(id_term1, id_term2, nasari_vectors)
        senses = [id_term1[indexes[0]], id_term2[indexes[1]] ] 
        max_similarities.append(max_similarity)
        best_senses.append(senses)
    return max_similarities, best_senses
"""
Find the list of babelnet ids from file SemEval17_IT_senses2synsets
Input:
    term: the word for which we need babelnet ids
    sense_to_synsets: list in the form [[word1,[babelnet ids]],...[wordn, [babelnet ids]]]
Output:
    List of babelnet ids (l[1])
"""
def findIds(term, sense_to_synsets):
    for l in sense_to_synsets:
        if term == l[0]:
            return l[1]            
    return None

"""
Associate a babelnet id to its embedded nasari vector 
Input:
    nasari_vectors: list of nasari vector
    babel_id: the babelnet id in the form bn:xxxxxxxxn
Output:
    a nasari vector (essentially a float vector)
"""
def findNasariVector(nasari_vectors, babel_id):
    sep = '__'
    for v in nasari_vectors:
        key = v[0].split(sep, 1)[0]
        if key == babel_id:
            return v[1:-1]
    return None
"""
Calculate the max cosine similarity between two words (expressed in the form of list of babelnet ids) 
Input:
    ids1 = list of babelnet ids
    ids2 = list of babelnet ids
    nasari_vectors: list of nasari vector
Output:
    max_similarity: the max value for the cosine similarity
    indexes: the indices of the two sense that have maximized the cosine similarity
"""
def calculateMaxSimilarity(ids1, ids2, nasari_vectors):
    #nasari_vectors = ut.importTsv('./tsvFiles/mini_NASARI.tsv')
    max_similarity = 0
    index1 = 0
    index2 = 0
    for i in range(len(ids1)):
        vect1 = findNasariVector(nasari_vectors, ids1[i])
        if not vect1:
            continue
        for j in range(len(ids2)):
            vect2 = findNasariVector(nasari_vectors, ids2[j])
            if not vect2: 
                continue
            cosine_similarity = calculateCosineSimilarity(vect1, vect2)
            if cosine_similarity>max_similarity:
                max_similarity = cosine_similarity
                index1 = i
                index2 = j
    indexes = [index1, index2]
    return max_similarity, indexes
"""
Calculate cosine similarity between two float vector (embedded nasari vectors) 
Input:
    vector1: an embedded nasari vector
    vector2: an embedded nasari vector
Output:
    sim: the cosine similarity value
"""
def calculateCosineSimilarity(vector1, vector2):
    x = np.array(vector1, dtype=float)
    y = np.array(vector2, dtype=float)
    sim = np.inner(x, y)/(norm(x) * norm(y))
    return sim
"""
Get only the annotated similarity value from the similarity list  
Input:
    list_sim: list in the form [[term1, term2, annotated similarity score]
Output:
    similarities: a list of similarity values
"""
def getSimilarities(list_sim):
    similarities = []
    for l in list_sim:
        similarities.append(float(l[2]))
    max_score = max(similarities)
    similarities = [w/max_score for w in similarities]
    return similarities
"""
Calculate Pearson and Spearmann correlation between the annotated similarity values and the automatic ones  
Input:
    automatic_similarities: list of similarity values between words
    personal_similarities: list of similarity values between words
Output:
    pearson_corr: Pearson correlation between the lists
    spearman_corr: Spermann correlation between the lists
"""
def calculateCorrelation(automatic_similarities, personal_similarities):
    indices = [i for i, x in enumerate(automatic_similarities) if not x]
    max_sim_not_none = [x for x in automatic_similarities if x is not None]
    similarities = getSimilarities(personal_similarities)
    #there are some none values in the automatic similarites, so i need to make the two list
    #of the same length, after have removed the none values from the automatic similarities list
    similarities = [i for j, i in enumerate(similarities) if j not in indices]
    pearson_corr, _ = pearsonr(similarities, max_sim_not_none)
    spearman_corr, _ = spearmanr(similarities, max_sim_not_none)
    return pearson_corr, spearman_corr