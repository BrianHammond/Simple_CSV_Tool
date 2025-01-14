# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#
# nothing special here

import csv
import os

class Misc:
    def __init__(self, folder, file):
        self.folder = folder
        self.file = file
        self.full_path = self.folder + "/" + self.file

class Folder(Misc):
    def check(self):
        if not os.path.isdir(self.folder):
                print(f"{self.folder} not found, creating folder")
                os.makedirs(self.folder)

class Information(Misc):
    def __init__(self, folder, file):
        super().__init__(folder, file)
        self.name = input("Name: ")
        self.title = input("Title: ")
        self.department = input("Department: ")

    def write(self):
        employees = [
            ["Name", "Title", "Department"],
            [self.name, self.title, self.department]
        ]

        with open(self.full_path, "w", newline="") as file:
            writer = csv.writer(file)
            for row in employees:
                writer.writerow(row)
            print("csv was created")

    def append(self):
        data_to_append = [
            [self.name, self.title, self.department]
        ]
        file = open(self.full_path, "a", newline="" )
        writer = csv.writer(file)
        writer.writerows(data_to_append)
        file.close()