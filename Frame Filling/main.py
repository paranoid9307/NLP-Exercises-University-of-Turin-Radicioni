import lesk as lk
import frames as fm
import evaluation as ev

list_of_frames = [1178, 189, 2113, 1017, 2972]
results = []
for id in list_of_frames:
    name_syn, elem_syn, lu_syn = lk.getFrameSynsets(id)
    frame_name, frame_el, frame_lus = fm.getFrameWords(id)
    s = {
        'name': frame_name,
        'synsetName': name_syn,
        'Elements': frame_el,
        'synsetElements': elem_syn,
        'Lexical units': frame_lus,
        'synsetLu': lu_syn
    }
    results.append(s)

with open('./output/Output Frame Filling.txt','w') as file:    
    for s in results:     
        file.write(str(s))
        file.write("\n")    
list_percentage = ev.evaluation(results)
print(list_percentage)
with open('./output/Accuracy Frame Filling.txt','w') as file: 
    i = 1   
    for p in list_percentage:     
        file.write("The accuracy for the frame "+ str(i) + " is : "+ str(p))
        file.write("\n")  
        i+=1  
