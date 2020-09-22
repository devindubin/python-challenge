import csv

file_path = 'Resources/election_data.csv'

with open(file_path) as file:
    for row in file:
        print(row)