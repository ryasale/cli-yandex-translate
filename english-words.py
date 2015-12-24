import csv
import random
import os

ya_dict = os.environ['YANDEX_TRANSLATE_DICTIONARY_FILE']
google_dict = os.environ['GOOGLE_PHRASEBOOK_DICTIONARY_FILE']

res_list = []
with open(google_dict, 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        s = row[2] + ' | ' + row[3]
        res_list.append(s)
with open(ya_dict, 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        s = row[2] + ' | ' + row[3]
        res_list.append(s)
print(random.choice(res_list))
