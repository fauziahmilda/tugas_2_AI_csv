import csv

rows = []

with open('data_2_ozi.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    #for row in csvreader:
    #    rows.append(row)
    rows = list(csvreader)
    print('total baris : ', csvreader.line_num)
    
for row in rows[:14]:
    print(row['nama'] + "\t-\t" +row['skill']+ "\t-\t" +row['power'])