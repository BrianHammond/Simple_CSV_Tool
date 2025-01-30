# checks to see if the 'PyQT6' module is installed
try: 
    from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
    from PyQt6 import uic
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("PyQT6 module is not installed")
    import subprocess
    required_packages = ['PyQT6']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt6 import uic
import csv

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) #load the UI file
        
        #buttons
        self.newFile_button.clicked.connect(self.newFile) # used to create a new .csv file
        self.select_button.clicked.connect(self.select) # used to open a .csv file
        self.submit_button.clicked.connect(self.submit) # used to append to a .csv file

        #menu bar
        self.about_action.triggered.connect(self.help_about)
       
    def help_about(self):
        self.window = QMainWindow()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()

    def newFile(self):
        self.table.setRowCount(0) # clears the table
        self.filename = QFileDialog.getSaveFileName(self, 'create a new file', '', 'Data File (*.csv)',)
        self.setWindowTitle(self.filename[0].split('/')[-1])

        employees = [
            ["Name", "Title", "Department",]
        ]

        try:
            with open(self.filename[0], "w", newline="") as file:
                writer = csv.writer(file)
                for row in employees:
                    writer.writerow(row)
        except FileNotFoundError:
            pass

    def submit(self):
        name = self.name_edit.text()
        title = self.title_edit.text()
        department = self.department_edit.text()

        if self.table.rowCount != 0:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(title))
            self.table.setItem(row, 2, QTableWidgetItem(department))

        data_to_append = [
            [name, title, department]
        ]
        try:
            with open(self.filename[0], "a", newline="" ) as file:
                writer = csv.writer(file)
                writer.writerows(data_to_append)
                print(f"info saved")
                file.close()
        except AttributeError:
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")
        self.name_edit.clear() 
        self.title_edit.clear() 
        self.department_edit.clear() 

    def select(self):
        self.filename = QFileDialog.getOpenFileName(self, 'create a new file', '', 'Data File (*.csv)',)
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            with open(self.filename[0], "r") as file:
                csvFile = csv.reader(file)
                next(file) # skips the header

                row = 0
                for line in csvFile: # i want to include the header information on each line with each value
                    name = line[0]
                    title = line[1]
                    department = line[2]

                    self.table.insertRow(row)
                    self.table.setItem(row, 0, QTableWidgetItem(name))
                    self.table.setItem(row, 1, QTableWidgetItem(title))
                    self.table.setItem(row, 2, QTableWidgetItem(department))
                    
                    print(f"Index = {row}, Name = {name}, Title = {title}, Department = {department}")

                    row += 1
        except FileNotFoundError:
            pass

# Show/Run app
if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    UIWindow = UI()
    UIWindow.show()
    sys.exit(app.exec())