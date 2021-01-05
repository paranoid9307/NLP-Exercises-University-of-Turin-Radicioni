import frames as fm
import nltk
from nltk.corpus import wordnet as wn

"""
Method that return most probable synsets for the various parts of the frame 
Input:
    frame_id: id of the frame that we use to get frame data from framenet
Output:
    name_syn: the most probable synset for the name of the frame
    elem_syn: list of most probable synset for the given elements' names
    lu_syn: list of most probable synsets for the given lexical units' names
"""   
def getFrameSynsets(frame_id):
    frame_name, frame_elements, frame_lus, frame_ctx = fm.getFrameData(frame_id)
    name_syn = getNameSynset(frame_name, frame_ctx)
    elem_syn = getElementSynsets(frame_elements, frame_ctx)
    lu_syn = getLuSynsets(frame_lus, frame_ctx)
    return name_syn, elem_syn, lu_syn

"""
Method that return most probable synset for the frame name
Input:
    frame_name: the name of the frame that we get from framenet
    frame_ctx: context of the frame
Output:
    the most prbable synset
"""   
def getNameSynset(frame_name, frame_ctx):
    if "_" in frame_name:   # Disambiguation needed
        frame_name=frame_name.replace("_", " ")
        if not wn.synsets(frame_name):
            pos_tags = getPOS(frame_name)
            name = getMainTerm(pos_tags)
        else:
            name = frame_name    
    else:
        name = frame_name
    synset = lesknltk(frame_ctx, name )    
    return synset.name()
"""
Method that return a list of probable synsets for the various elements of the frame
Input:
    frame_elements: the elements' names that we get from framenet
    frame_ctx: context of the frame
Output:
    elem_syn: list of most probable synset for the given elements' names
"""
def getElementSynsets(frame_elements, frame_ctx):
    if not frame_elements:
        return None
    elem_syn = []
    for elem in frame_elements:
        elem_def = fm.bagOfWords(frame_elements[elem].definition)
        if "_" in elem:
            elem=elem.replace("_", " ")
            if not wn.synsets(elem):
                pos_tags = getPOS(elem)
                elem = getMainTerm(pos_tags)  
        elem_ctx = frame_ctx.union(elem_def)
        elem_syn.append(lesknltk(elem_ctx, elem).name())
    return elem_syn   
"""
Method that return a list of probable synsets for the various lexical units of the frame
Input:
    frame_lus: the lexical units' names that we get from framenet
    frame_ctx: context of the frame
Output:
    lu_syn: list of most probable synsets for the given lexical units' names
"""
def getLuSynsets(frame_lus, frame_ctx):
    if not frame_lus:
        return None
    lu_syn = []
    keys = frame_lus.keys()
    for k in keys:
        ambiguous_word = frame_lus[k].lexemes[0].name
        lu_def = fm.bagOfWords(frame_lus[k].definition)
        lu_ctx = frame_ctx.union(lu_def)
        synset = lesknltk(lu_ctx, ambiguous_word)
        if not synset: 
            lu_syn.append(synset)
        else: 
            lu_syn.append(synset.name())        
    return(lu_syn)

#Part of speech of the name or the elements of the frame, that can contains more than a word
def getPOS(frame_term):    
    pos_tags=nltk.pos_tag(nltk.word_tokenize(frame_term), tagset='universal')
    return pos_tags
#get the noun or the verb or the noun in an expression
def getMainTerm(pos):
    for word, tag in pos:
        if tag == "VERB":
            return word
        elif tag == "NOUN":
            return word
"""
Get the most probable sense of a word in a sentence based on the constructed context
Input:
    context_sentence: the context of the frame part that we need to disambiguate 
    (definition of frame and definition of the part like element or lexical unit)
    ambiguous_word: the word we need to find the synset for
Output:
    sense: the most probable synset
"""
def lesknltk(context_sentence, ambiguous_word):
    context = set(context_sentence)
    synsets = wn.synsets(ambiguous_word)
    if not synsets:
        return None
    _, sense = max((len(context.intersection(set(getSynsetContext(ss)))), ss) for ss in synsets)
    return sense
"""
Get processed context of the given synset
(synset examples, synset hypernym and hyponym definitions and examples and synset definition)
Input:
   s: a wordnet synset
Output:
    context: a list containing all the processed words that begin to the context of the synset
"""
def getSynsetContext(s):
    context=fm.bagOfWords(s.definition())
    for e in s.examples():
        context=list(set().union(context, fm.bagOfWords(e)))
    for hypernym in s.hypernyms():
        context=list(set().union(context, fm.bagOfWords(hypernym.definition())))
        for e in hypernym.examples():
            context=list(set().union(context, fm.bagOfWords(e)))
    for hypo in s.hyponyms():
        context=list(set().union(context, fm.bagOfWords(hypo.definition())))
        for e in hypo.examples():
            context=list(set().union(context, fm.bagOfWords(e)))
    return context
