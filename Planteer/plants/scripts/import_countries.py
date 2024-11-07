import os
import django
import csv
from plants.models import Country

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Planteer.settings")
django.setup()
csv_file_path = 'plants/data/countries.csv'

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file) 
    
    for row in reader:
        country_name = row['Name'] 
        alpha_code = row['Code']  
        
        Country.objects.get_or_create(name=country_name, alpha_code=alpha_code)
