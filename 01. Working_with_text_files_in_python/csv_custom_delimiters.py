import csv

with open('passwd.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)