import csv
import datetime
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from main_ui import Ui_MainWindow as main_ui
from about_window import AboutWindow

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #buttons
        self.newFile_button.clicked.connect(self.create_file) # used to create a new .csv file
        self.select_button.clicked.connect(self.select_file) # used to open a .csv file
        self.submit_button.clicked.connect(self.submit_file) # used to append to a .csv file

        #menu bar
        self.about_action.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

        # text fields
        self.name = self.name_edit
        self.title = self.title_edit
        self.department = self.department_edit

    def create_file(self):
        self.table.setRowCount(0) # clears the table
        self.filename = QFileDialog.getSaveFileName(self, 'create a new file', '', 'Data File (*.csv)',)
        self.setWindowTitle(self.filename[0].split('/')[-1])

        employees = [
            ["Name", "Title", "Department", "Timestamp"]
        ]

        try:
            with open(self.filename[0], "w", newline="") as file:
                writer = csv.writer(file)
                for row in employees:
                    writer.writerow(row)
        except FileNotFoundError:
            pass

    def submit_file(self):
        self.current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")

        name = self.name.text()
        title = self.title.text()
        department = self.department.text()
        timestamp = self.current_date

        row = self.table.rowCount()
        
        self.populate_table(row, name, title, department, timestamp)

        data_to_append = [
            [name, title, department, timestamp]
        ]
        try:
            with open(self.filename[0], "a", newline="" ) as file:
                writer = csv.writer(file)
                writer.writerows(data_to_append)
                file.close()
        except AttributeError:
            self.clear_fields(self.name, self.title, self.department)
            self.table.setRowCount(0) # clears the table
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")
        except FileNotFoundError:
            self.clear_fields(self.name, self.title, self.department)
            self.table.setRowCount(0) # clears the table
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")

        self.clear_fields(self.name, self.title, self.department)

    def select_file(self):
        self.clear_fields(self.name, self.title, self.department)
        self.table.setRowCount(0) # clears the table
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
                    timestamp = line[3]

                    self.populate_table(row, name, title, department, timestamp)

                    row += 1
        except FileNotFoundError:
            pass
    
    def populate_table(self, row, name, title, department, timestamp):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(title))
        self.table.setItem(row, 2, QTableWidgetItem(department))
        self.table.setItem(row, 3, QTableWidgetItem(timestamp))

    def clear_fields(self, name, title, department):
            name.clear() 
            title.clear() 
            department.clear()

    def about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def about_qt(self):
        QApplication.aboutQt()

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
    