import csv

class CSVReader:

    def __init__(self):
        super().__init__()

    def getData(self):
        with open('tests/map1.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            result = []
            for row in readCSV:
                result.append(row)
            print(result[1:])