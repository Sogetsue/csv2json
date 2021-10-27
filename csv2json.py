import csv
import json


# In shell, call like from csv2json import csvtojson
# csvtojson("<path>").convert_2_json()
class csvtojson():
    def __init__(self, csv_file):
        self.csv_file = str(csv_file)

    def convert_2_json(self, **options):
        json_data = []
        print(self.csv_file)
        output_file = self.csv_file.replace('.csv', '.txt')
        with open(self.csv_file, 'r') as ifile:
            csv_read = csv.DictReader(ifile)
            keys = csv_read.fieldnames
            for row in csv_read:
                dict = {}
                for key in keys:
                    dict[key] = row[key]
                json_data.append(dict)
        with open(output_file, 'w') as ofile:
            json.dump(json_data, ofile)
            
