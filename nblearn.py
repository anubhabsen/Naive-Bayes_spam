import json
# from nltk.stem import PorterStemmer
import os
import sys
from operator import add
import glob

# ps = PorterStemmer()
spam_words = 0
ham_words = 0
spams = 0
hams = 0
master_dict = {}
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def readtodict(filename, clas):
    if clas == 'spam':
        global spams
        spams += 1
    else:
        global hams
        hams += 1
    with open(filename, "r", encoding="latin1") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for line in content:
        x = line.split()
        for j in x:
            # if not j.isalnum() or j.isdigit() or j.lower() in stop_words:
            #     continue
            if clas == 'spam':
                master_dict[j.lower()] = list(map(add, master_dict.get(j.lower(), [0, 0, 0]), [1, 0 ,1]))
                global spam_words
                spam_words += 1
            elif clas == 'ham':
                master_dict[j.lower()] = list(map(add, master_dict.get(j.lower(), [0, 0, 0]), [0, 1 ,1]))
                global ham_words
                ham_words += 1

root_dir = sys.argv[1]
root_dir = os.path.abspath(root_dir)
for file in glob.iglob(root_dir + '/**/*', recursive=True):
    if file.endswith('.txt'):
        if 'spam' in file:
            readtodict(file, 'spam')
        if 'ham' in file:
            readtodict(file, 'ham')

vocab_size = len(master_dict)
for i in master_dict:
    master_dict[i][0] = (master_dict[i][0] + 1) / (spam_words + vocab_size)
    master_dict[i][1] = (master_dict[i][1] + 1) / (ham_words + vocab_size)

if spams + hams == 0:
    spam_p = 0
    ham_p = 0
else:
    spam_p = spams / (spams + hams)
    ham_p = hams / (spams + hams)

with open('nbmodel.txt', 'w') as fp:
    json.dump([spam_p, ham_p, master_dict], fp)