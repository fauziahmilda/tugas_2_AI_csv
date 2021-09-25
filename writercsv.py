import csv
from os import write

rows = [
    {'nama' : 'kate', 'skill' : 'fire ball', 'power' : 100,},
    {'nama' : 'nuga', 'skill' : 'air punch', 'power' : 95,},
    {'nama' : 'luna', 'skill' : 'empath mind', 'power' : 100,},
    {'nama' : 'jhon', 'skill' : 'fire arrow', 'power' : 200,},
    {'nama' : 'puma', 'skill' : 'unseen light', 'power' : 100,},
    {'nama' : 'alex', 'skill' : 'water splash', 'power' : 200,},
    {'nama' : 'pette', 'skill' : 'unseen sword', 'power' : 250,},
    {'nama' : 'emme', 'skill' : 'holo water', 'power' : 150,},
    {'nama' : 'abra', 'skill' : 'water arrow', 'power' : 200,},
    {'nama' : 'keyl', 'skill' : 'iron body', 'power' : 250,},
]

with open('data_2_ozi.csv', 'a') as csvfile:
    fields = ['nama', 'skill', 'power']
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(rows)