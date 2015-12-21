import csv
import random
import os

file_name_ya_dict = 'yandex-translate-dictionary.csv'
file_name_google_phrasebook = 'google-translate-phrasebook.csv'
file_path = os.path.dirname(os.path.realpath(__file__))
res_list = []
with open(os.path.join(file_path, file_name_google_phrasebook), 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        s = row[2] + ' | ' + row[3]
        res_list.append(s)
with open(os.path.join(file_path, file_name_ya_dict), 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        s = row[2] + ' | ' + row[3]
        res_list.append(s)
print(random.choice(res_list))