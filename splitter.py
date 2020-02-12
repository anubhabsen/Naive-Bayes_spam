from shutil import copyfile
from random import sample
import os
import glob

cwd = os.getcwd()
root = "Spam_or_Ham"
os.chdir(root)

train = []
for file in glob.iglob('**/*', recursive=True):
    if ('train/' in file) and file.endswith('.txt'):
        train.append(file)

tot = round(len(train) * 0.1)
spam_num = tot // 2
ham_num = tot - spam_num

spam = []
ham = []

for file in train:
    if '/spam/' in file:
        spam.append(file)
    else:
        ham.append(file)

if len(spam) < spam_num:
    spam_num = len(spam)
    ham_num = tot - spam_num
if len(ham) < ham_num:
    ham_num = len(ham)
    spam_num = tot - ham_num

spam_selected = sample(spam, spam_num)
ham_selected = sample(ham, ham_num)

count = 0
for i in spam_selected:
    src = cwd + '/' + root + '/' + i
    print('cp ' + src + ' 10pdata/' + str(count) + 'spam.txt;')
    count += 1

for i in ham_selected:
    src = cwd + '/' + root + '/' + i
    print('cp ' + src + ' 10pdata/' + str(count) + 'ham.txt;')
    count += 1