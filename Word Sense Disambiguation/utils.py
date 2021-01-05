import csv
import re

# import senntences to analyze as a dictionary containing the sentence and the ambiguous word
def openFile(path):
    sentences = []
    file = open(path, 'r')
    for line in file.readlines():
        to_analyze = re.search('\\*[^\\*]+\\*', line).group(0).strip('**').lower()
        line = re.sub('[-\\*\\n.]', '', line).lower().strip()
        sentences.append({'sentence': line, 'word': to_analyze})
    file.close()
    return sentences


