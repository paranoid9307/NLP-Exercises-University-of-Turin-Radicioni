#five manually annotated frame in the form of a dictionary

frame1 = {'name': 'Interior_profile_relation', 
'synsetName': 'inside.n.01', 
'Elements': ['Figure', 'Ground', 'Time', 'Direction', 
'Accessibility', 'Profiled_region', 'Directness', 
'Temporal_profile', 'Deixis', 'Region_quantification'], 
'synsetElements': ['figure.n.11', 'land.n.04', 
'time.v.02', 'direction.n.03', 'handiness.n.02', 
'region.n.01', 'directness.n.01', 'temporal_role.n.01', 
'deixis.n.01', 'region.n.04'], 
'Lexical units': ['in', 'inside', 'among', 'within', 'between', 
'amid', 'in', 'in', 'outside', 'outside'], 
'synsetLu': ['inside.n.01', 'inside.n.01', None, 
'inside.r.02', 'between.r.02', None, 
'inside.n.01', 'inside.n.01', 'outside.s.05', 'outside.s.05']}
 
frame2 ={'name': 'Quantified_mass', 
'synsetName':  'mass.n.02', 
'Elements': ['Quantity', 'Mass', 'Individuals', 'Q_prop', 'Degree'],
'synsetElements': [ 'quantity.n.01',  'mass.n.01', 
 'person.n.01',  'q.n.01',  'degree.n.07'], 
'Lexical units': ['oodles', 'pile', 'ton', 'heap', 'load', 'modicum', 
'mite', 'mass', 'scads', 'hundreds', 'thousands', 'millions', 'billion', 
'dozens', 'shitload', 'abundance', 'myriad', 'plethora', 'quantity', 'number', 
'pinch', 'ounce', 'touch', 'measure', 'amount', 'scores', 'degree', 'avalanche', 
'deluge', 'torrent', 'flood', 'trickle', 'stream', 'wave', 'raft', 'mountain', 'handful', 
'a', 'few', 'many', 'several', 'several', 'few', 'a', 'any', 'many', 'all', 'numerous', 
'a', 'no', 'multiple', 'dose', 'a', 'both', 'smattering', 'fair', 'trace', 'deal'], 
'synsetLu': [ 'tons.n.01',  'batch.n.02',  'tons.n.01',  'batch.n.02', 
 'load.n.02',  'modicum.n.01',  'touch.n.06',  'batch.n.02', 
 'tons.n.01',  'hundred.n.01',  'thousand.n.01',  'million.n.02', 
 'million.n.02',  'tons.n.01', None,  'abundance.n.01',  'myriad.n.01', 
 'overplus.n.01',  'quantity.n.02',  'number.n.01',  'touch.n.06', 
 'ounce.n.01',  'touch.n.06',  'measure.n.02', 
 'measure.n.02',  'tons.n.01',  'degree.n.01',  'avalanche.n.02', 
 'deluge.n.01',  'torrent.n.03',  'flood.n.02',  'trickle.n.01', 
 'stream.n.04',  'wave.n.02',  'batch.n.02',  'batch.n.02', 
 'handful.n.01',  None,  'few.n.01', 
 'many.a.01',  'several.s.01',  'several.s.01',  'few.n.01', 
 None,  'any.s.01',  'many.a.01', 
 'all.a.01',  'numerous.s.01',  None, 
 'no.a.01',  'multiple.a.01',  'dose.n.02', 
 None,  'both.s.01',  'handful.n.01', 
 'fair.a.02',  'trace.n.01',  'batch.n.02']
 }
 
#forse se fa ricerca su entrambi i termini (qualora il termine fosse multiword) otterremmo risultati migliori
frame3 = {'name': 'History', 
'synsetName': 'history.n.02', 
'Elements': ['Topic', 'Domain', 'End_time', 'Start_time', 'Time_span', 'Duration', 'Time'], 
'synsetElements': ['topic.n.01', 'domain.n.05', 'end.n.03', 
'start.n.01',  'span.n.01',  'duration.n.01', 'time.n.01'], 
'Lexical units': ['history'], 
'synsetLu': ['history.n.02']
}

frame4 = {'name': 'Noise_makers', 
'synsetName': 'noise.n.02', 
'Elements': ['Noise_maker', 'Use', 'Creator', 'Time_of_creation', 'Name', 'Type', 'Material', 'Ground'], 
'synsetElements': ['noise.n.02', 'use.n.02', 'creator.n.02', 'time.v.05', 
'name.v.01', 'type.n.01', 'fabric.n.01', 'ground.n.08'], 
'Lexical units': ['guitar', 'bell', 'siren', 'piano', 'rattle', 'xylophone', 'drum', 'cello', 
'saxophone', 'alarm'], 
'synsetLu': ['guitar.n.01', 'bell.n.01', 'siren.n.04', 'piano.n.01', 
'rattle.v.02', 'marimba.n.01', 'drum.n.01', 'cello.n.01', 
'sax.n.02', 'alarm.n.03']
}

frame5 = {'name': 'Transition_to_a_quality', 
'synsetName': 'transition.n.03', 
'Elements': ['Place', 'Time', 'Duration_of_final_state', 'Manner', 'Entity', 
'Final_quality', 'Transitional_period', 'Circumstances', 'Group', 'Explanation'], 
'synsetElements': ['place.n.01', 'time.n.01', 'duration.n.03', 
'manner.n.03', 'entity.n.01', 'quality.n.01', 
'period.n.01', 'context.n.02', 'group.n.03', 'explanation.n.01'], 
'Lexical units': ['go'], 
'synsetLu': ['go.v.04']
}

"""
Get percentage of similarity between the annotated frame parts and the automatic ones
Input:
   results: a list of 5 dictionaries containing the results of the computation.
Output:
    percentage1: similarity between annotated synsets for frame 1 and automatically taken synsets for frame 1
    percentage2: similarity between annotated synsets for frame 2 and automatically taken synsets for frame 2
    percentage3: similarity between annotated synsets for frame 3 and automatically taken synsets for frame 3
    percentage4: similarity between annotated synsets for frame 4 and automatically taken synsets for frame 4
    percentage5: similarity between annotated synsets for frame 5 and automatically taken synsets for frame 5
"""
def evaluation(results):
    frame1_auto = results[0]
    frame2_auto = results[1]
    frame3_auto = results[2]
    frame4_auto = results[3]
    frame5_auto = results[4]

    percentage1 = confront(frame1, frame1_auto)
    percentage2 = confront(frame2, frame2_auto)
    percentage3 = confront(frame3, frame3_auto)
    percentage4 = confront(frame4, frame4_auto)
    percentage5 = confront(frame5, frame5_auto)

    return percentage1, percentage2, percentage3, percentage4, percentage5
"""
Calculate percentage of similarity between the annotated frame parts and the automatic ones
Input:
   frame_ann: the dictionary manually annotated containing the synsets choosen for the various part of the frame
   frame_aut: the dictionary automatically annotated containing the synsets choosen for the various part of the frame
Output:
    round(percentage,2): the rounded percentage of similarity 
"""
def confront(frame_ann, frame_aut):
    count = 0    
    synset_name_ann = frame_ann['synsetName']
    synset_name_aut = frame_aut['synsetName']
    synset_element_ann = frame_ann['synsetElements']
    synset_element_aut = frame_aut['synsetElements']
    synset_lus_ann = frame_ann['synsetLu']
    synset_lus_aut = frame_aut['synsetLu']

    total_len = len(synset_element_aut) + len(synset_lus_aut) + 1
    if synset_name_ann == synset_name_aut: count+=1
    count += len([s for s in synset_element_aut if s in synset_element_ann])
    count += len([s for s in synset_lus_aut if s in synset_lus_ann])
    percentage = (count/total_len)*100
    return round(percentage,2)