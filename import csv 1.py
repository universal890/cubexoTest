import csv

def create_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data[0].keys())  
        for row in data:
            writer.writerow(row.values())

data = [
{'name': 'aman', 'age': 30},
{'name': 'jatin', 'age': 25},
{'name': 'nikil', 'age': 20},
{'name': 'vivek', 'age': 23},
{'name': 'divyansh', 'age': 21},
{'name': 'shaury', 'age': 26},
{'name': 'durgesh', 'age': 22},
{'name': 'rushabh', 'age': 24},
{'name': 'udit', 'age': 27},
{'name': 'snehil', 'age': 29},
]
create_csv('new_data.csv', data)
 