import csv
from your_app_name.models import YourModel

def import_csv_data(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            YourModel.objects.create(**row)

import_csv_data('new data.csv')