import json
import os
import sys
from operator import add

spam = {}
ham = {}
allmails = {}
spam_words = 0
ham_words = 0
tot_words = 0
master_dict = {}

def readtodict(filename, dictionary, clas):
	with open(filename, "r", encoding="latin1") as f:
	    content = f.readlines()
	content = [x.strip() for x in content]
	for line in content:
		x = line.split()
		for j in x:
			master_dict[j.lower()] = master_dict.get(j.lower(), [0, 0, 0]) +
			dictionary[j.lower()] = dictionary.get(j.lower(), 0) + 1
			global tot_words
			tot_words += 1
			if clas == 'spam':
				global spam_words
				spam_words += 1
			elif clas == 'ham':
				global ham_words
				ham_words += 1
			allmails[j.lower()] = allmails.get(j.lower(), 0) + 1

# root_dir = sys.argv[1]
root_dir = "Spam or Ham"
root_dir += '/train/'

for i in os.listdir(root_dir):
	for j in os.listdir(root_dir + i +'/'):
		if j == 'ham':
			for k in os.listdir(root_dir + i +'/' + j + '/'):
				filename = root_dir + i +'/' + j + '/' + k
				readtodict(filename, ham, 'ham')
		elif j == 'spam':
			for k in os.listdir(root_dir + i +'/' + j + '/'):
				filename = root_dir + i +'/' + j + '/' + k
				readtodict(filename, spam, 'spam')

# for i in allmails:
# 	if spam.get(i, 0) + ham.get(i, 0) != allmails[i]:
# 		print(i)

for i in spam:
	spam[i] = spam[i] / spam_words

for i in ham:
	ham[i] = ham[i] / ham_words

all_data = {'spam': spam, 'ham': ham, 'allmails': allmails, 'spam_words': spam_words, 'ham_words': ham_words, 'tot_words': tot_words}

with open('nbmodel.txt', 'w') as fp:
    json.dump(all_data, fp)
