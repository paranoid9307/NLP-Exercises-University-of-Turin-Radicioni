import csv

#load a csv file
def load_csv(path):
    couple_list = []
    with open(path, 'r') as fileCSV:
        for row in fileCSV.readlines()[1:]:
            temp = row.split(",")
            gold_value = temp[2].replace('\n', '')
            couple_list.append((temp[0], temp[1], float(gold_value)/10))
    return couple_list
    
#write a table on a file
def writeTable(table, path):
    data = table.get_string()
    with open(path, 'w') as f:
        f.write(data)

