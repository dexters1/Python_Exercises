import csv
from collections import defaultdict

columns = defaultdict(list)

with open('zadatak_csv.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)
            
print(columns['Title'], columns["Release Date"])

with open("movies.txt", "w") as f:
    for (k,v) in zip(columns["Title"], columns["Release Date"]):
        f.write("%s:%s\n" %(k, v))