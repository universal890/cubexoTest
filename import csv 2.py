import csv

data = [
    {'name': 'Harsh', 'age': 30, 'url': ''},
    {'name': 'jatin', 'age': 25, 'url': ''},
    {'name': '', 'age': 35, 'url': ''}
]

csv_file_path = 'data.csv'

fieldnames = ['name', 'age', 'city']

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  
    writer.writerows(data) 