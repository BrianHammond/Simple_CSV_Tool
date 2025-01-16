# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#
# nothing special here

import csv

class Misc:
    def __init__(self, csv_folder, csv_file):
        self.csv_folder = csv_folder
        self.csv_file = csv_file
        self.csv_full_path = self.csv_folder + "/" + self.csv_file

class Write_Append(Misc):
    def __init__(self, csv_folder, csv_file):
        super().__init__(csv_folder, csv_file)
        self.csv_name = input("Name: ")
        self.csv_title = input("Title: ")
        self.csv_department = input("Department: ")

    def write(self):
        employees = [
            ["Name", "Title", "Department", "Index"],
            [self.csv_name, self.csv_title, self.csv_department]
        ]

        with open(self.csv_full_path, "w", newline="") as file:
            writer = csv.writer(file)
            for row in employees:
                writer.writerow(row)
            print("csv was created")

    def append(self):
        data_to_append = [
            [self.csv_name, self.csv_title, self.csv_department]
        ]
        file = open(self.csv_full_path, "a", newline="" )
        writer = csv.writer(file)
        writer.writerows(data_to_append)
        file.close()

class Read_CSV(Misc):
    def read(self):
       
        with open(self.csv_full_path, "r") as file:
            content = csv.reader(file)
            next(file) # skips the header
            index_num = 1
            for line in content: # i want to include the header information on each line with each value
                print(f"Index = {index_num}, Name = {line[0]}, Title = {line[1]}, Department = {line[2]}")
                index_num += 1