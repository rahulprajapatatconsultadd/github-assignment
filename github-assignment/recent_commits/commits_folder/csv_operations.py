import pandas
from json import dumps
from pathlib import Path
from os.path import join
from csv import DictReader


class CsvOperation:
    
    def __init__(self):
        self.__file = Path(__file__).resolve().parent.parent.parent.parent
        # self.__json_file = join(self.__file, 'github_project','json','info.json')
        # self.__csv_file = join(self.__file, 'github_project','csv','all_commits.csv')
         
    
    def sort_csv(self):
        print("$$%%$")
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",self.__csv_file)
        # data = pandas.read_csv(self.__csv_file)
        data = pandas.read_csv("github_project/csv/all_commits.csv")
        print("Sorting$$@#data",data)
        sorted_csv = data.sort_values(by='date', ascending=False)
        sorted_csv.to_csv("github_project/csv/all_commits.csv", index=False)
        
        
    def csv_to_json(self):
        with open("github_project/csv/all_commits.csv", newline='') as csvfile:
            reader = DictReader(csvfile)
            csv_data = list()
            row_num = 500
            for row in reader:
                if row_num == 0:
                    break
                csv_data.append(row)
                row_num -= 1
                
        json_obj = dumps(csv_data, indent=4)
        with open("github_project/json/info.json", 'w') as jsonfile:
            jsonfile.write(json_obj)
