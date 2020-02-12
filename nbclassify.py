import json
import sys
import os
import glob
import math

correct_predicts = 0
output_string = ""
with open('nbmodel.txt', 'r') as fp:
	data = fp.read()

data = json.loads(data)
spam_p = data[0]
ham_p = data[1]
master_dict = data[2]

root = sys.argv[1]
pys = []
os.chdir(root)
for file in glob.iglob('**/*', recursive=True):
    if file.endswith('.txt'):
        pys.append(file)

for filename in pys:
	prob_s = math.log(spam_p)
	prob_h = math.log(ham_p)
	with open(filename, "r", encoding="latin1") as f:
	    content = f.readlines()
	content = [x.strip() for x in content]
	for line in content:
		x = line.split()
		for j in x:
			j = j.lower()
			if j not in master_dict:
				continue
			prob_s += math.log(master_dict[j][0])
			prob_h += math.log(master_dict[j][1])
	if prob_s > prob_h:
		output_string += 'spam ' + filename + '\n'
		# print('spam ' + filename)
		if filename.endswith('.spam.txt'):
			correct_predicts += 1
	else:
		output_string += 'ham ' + filename + '\n'
		# print('ham ' + filename)
		if filename.endswith('.ham.txt'):
			correct_predicts += 1

tot_files = len(pys)
print(correct_predicts / tot_files * 100)
f = open("nboutput.txt", "w")
f.write(output_string)
f.close()