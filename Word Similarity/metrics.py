import nltk
import math
from nltk.corpus import wordnet as wn

"""
    Calculate the maximum similarity between words based on Wu-Palmer similarity metric
    Input:
        ss1: list of synsets of word
        ss2: list of synsets of word
    Output:
        max_wup_similarity: the maximum value between every similarity scores of the senses of the 2 words
    https://docs.huihoo.com/nltk/0.9.5/api/nltk.wordnet.similarity-pysrc.html#wup_similarity
"""
def wupSimilarity(ss1,ss2):
    max_wup_similarity = 0
    for syn in ss1:        
        hy1 = syn.hypernym_paths()        
        for sy in ss2:
            hy2 = sy.hypernym_paths()
            commons = commonHypernyms(hy1, hy2)
            lowest_common = lowestCommonSubsumer(commons)
            if not lowest_common:
                wup_similarity = 0
            else:
                lcd = lowest_common.min_depth()
                if lcd == 0: lcd = 1
                depth1 = syn.min_depth()
                depth2 = sy.min_depth()
                wup_similarity = (2 * lcd) / (depth1 + depth2)
            max_wup_similarity = max(wup_similarity, max_wup_similarity)    
    return max_wup_similarity 

"""
    Calculate the similarity between words based on Shortest Path similarity metric
    Input:
        ss1: list of synsets of word
        ss2: list of synsets of word
    Output:
        similarity
"""
def shortestPathSimilarity (ss1, ss2):
    distances = []
    max_depth = 20
    for s in ss1:
        for s1 in ss2:
            distances.append(minimumDistanceImproved(s,s1))
    distances = [x for x in distances if x is not None]
    if not distances:
        similarity = 0
    else:
        minimum_distance = min(distances)
        similarity = (2*max_depth - (minimum_distance))/(2*max_depth)
    return similarity

"""
    Calculate the maximum similarity between words based on Leacock Chodorow similarity metric
    Input:
        ss1: list of synsets of word
        ss2: list of synsets of word
    Output:
        Leacock chodorow similarity between the two words
"""            
def leakChodSimilarity (ss1, ss2):
    distances = []
    max_depth = 20
    for s in ss1:
        for s1 in ss2:
            distances.append(minimumDistanceImproved(s,s1))
    distances = [x for x in distances if x is not None]
    if not distances:
        similarity = 0
    else:
        minimum_distance = min(distances)
        if minimum_distance != 0:
            similarity = - (math.log(minimum_distance/(2*max_depth))) / math.log(2*max_depth + 1)
        else:
            similarity = - (math.log(minimum_distance + 1/(2*max_depth + 1))) / math.log(2*max_depth + 1)
    return similarity  

#create a set of common hypernyms of the 2 words in input
def commonHypernyms(hyp1, hyp2):
    hyp1 = [y for x in hyp1 for y in x]
    hyp2 = [y for x in hyp2 for y in x]
    common_hypernyms = set(hyp1).intersection(set(hyp2))
    return common_hypernyms

#Return the lowest common subsumer between two synsets, the one with the maximum distance from synset to root
def lowestCommonSubsumer(commons):
    lcd = 0   # lch depth  
    lch = None  # lowest common hypernyms
    for s in commons:
        m = maxDepth(s)
        if m > lcd:
            lcd = m
            lch = s
    return lch

#calculate the maximum depth of a synset
def maxDepth(synset):
  hypernymsPaths = synset.hypernym_paths()
  maxDepth = (max(len(path) for path in hypernymsPaths))
  return maxDepth

def minimumDistance(syn1, syn2):
  distance = 0
  equals = 0
  one_step = 1
  if syn1.name() == syn2.name():
      return equals
  hyp1 = syn1.hypernyms()
  hyp2 = syn2.hypernyms()  
  if hyp1 and hyp2 and hyp1[0].name() == hyp2[0].name():
      return one_step  
  while hyp1 and hyp2:
    if hyp1[0].name() == hyp2[0].name():
        return distance+1    
    hyp1 = hyp1[0].hypernyms()
    if not hyp1 :
        break
    elif hyp1[0].name() == hyp2[0].name():
        return distance+1
    hyp2 = hyp2[0].hypernyms()
    if not hyp2 :
        break
    elif hyp1[0].name() == hyp2[0].name():
        return distance+1 
  return None
"""
    Calculate the minimum distance between words based on Bfs algorithm
    Input:
        syn1: synset of word
        syn2: synset of word
    Output:
        distance between the two synsets on the wordnet tree
"""
def minimumDistanceImproved(syn1, syn2):
    distance = 0
    equals = 0
    one_step = 1

    #synsets are equals
    if syn1.name() == syn2.name():
        return equals

    #getting hypernyms of synsets
    hyp1 = syn1.hypernyms()
    hyp2 = syn2.hypernyms() 

    #synsets are at distance 1
    if hyp1 and hyp2 and hyp1[0].name() == hyp2[0].name():
        return one_step

    #loop to search the first level of the tree where the synsets are equal (bottom up)     
    while hyp1 and hyp2:
        distance+=1
        precHyp1 = hyp1[0].name()
        hyp1 = hyp1[0].hypernyms()
        if not hyp1: break
        distance+=1
        if hyp2[0].name() == precHyp1: return distance
        if hyp2[0].name() == hyp1[0].name: return distance+1
        hyp2 = hyp2[0].hypernyms()
        if not hyp2 : break
        if hyp2[0].name() == precHyp1: return distance+1
        if hyp2[0].name() == hyp1[0].name: return distance+2
    return None

