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
	if not (line.endswith('.spam.txt') or line.endswith('.ham.txt')):
		continue
	else:
		if line.startswith('spam'):
			if line.endswith('.spam.txt'):
				spam_correct += 1
			else:
				spam_incorrect += 1
		if line.startswith('ham'):
			if line.endswith('.ham.txt'):
				ham_correct += 1
			else:
				ham_incorrect += 1

# print order precision, recall, f1

spam_stat = [spam_correct / (spam_correct + ham_incorrect), spam_correct / (spam_correct + spam_incorrect), 0]
spam_stat[2] = spam_stat[0] * spam_stat[1] * 2 / (spam_stat[0] + spam_stat[1])

ham_stat = [ham_correct / (ham_correct + spam_incorrect), ham_correct / (ham_correct + ham_incorrect), 0]
ham_stat[2] = ham_stat[0] * ham_stat[1] * 2 / (ham_stat[0] + ham_stat[1])

print('spam', spam_stat)
print('ham', ham_stat)