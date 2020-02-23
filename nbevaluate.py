import sys

spam_correct = 0
spam_incorrect = 0
ham_correct = 0
ham_incorrect = 0
filename = sys.argv[1]
with open(filename, "r", encoding="latin1") as f:
	content = f.readlines()
content = [x.strip() for x in content]

for line in content:
	if not (line.endswith('spam.txt') or line.endswith('ham.txt')):
		continue
	else:
		if line.startswith('spam'):
			if line.endswith('spam.txt'):
				spam_correct += 1
			else:
				spam_incorrect += 1
		if line.startswith('ham'):
			if line.endswith('ham.txt'):
				ham_correct += 1
			else:
				ham_incorrect += 1

# print order precision, recall, f1

spam_stat = []
ham_stat = []
try:
	precision = spam_correct / (spam_correct + spam_incorrect)
	spam_stat.append(precision)
except:
	spam_stat.append("division by zero error")

try:
	recall = spam_correct / (spam_correct + ham_incorrect)
	spam_stat.append(recall)
except:
	spam_stat.append("division by zero error")

try:
	f1 = spam_stat[0] * spam_stat[1] * 2 / (spam_stat[0] + spam_stat[1])
	spam_stat.append(f1)
except:
	spam_stat.append("division by zero error")

try:
	precision = ham_correct / (ham_correct + ham_incorrect)
	ham_stat.append(precision)
except:
	ham_stat.append("division by zero error")

try:
	recall = ham_correct / (ham_correct + spam_incorrect)
	ham_stat.append(recall)
except:
	ham_stat.append("division by zero error")

try:
	f1 = ham_stat[0] * ham_stat[1] * 2 / (ham_stat[0] + ham_stat[1])
	ham_stat.append(f1)
except:
	ham_stat.append("division by zero error")

print('spam', spam_stat)
print('ham', ham_stat)