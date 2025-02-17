import csv
import datetime
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui

class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts
        
        #buttons
        self.button_new.clicked.connect(self.create_file) # used to create a new .csv file
        self.button_import.clicked.connect(self.import_file) # used to open a .csv file
        self.submit_button.clicked.connect(self.submit_file) # used to append to a .csv file

        #menu bar
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.about_action.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)

        # text fields
        self.name = self.line_name
        self.title = self.line_title
        self.department = self.line_department

    def create_file(self):
        self.table.setRowCount(0) # clears the table
        self.filename = QFileDialog.getSaveFileName(self, 'create a new file', '', 'Data File (*.csv)',)

        if not self.filename[0]:
            return  # Do nothing if no file is selected
        
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            with open(self.filename[0], "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Title", "Department", "Timestamp"])  # Directly writing header
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

        data_to_append = [[name, title, department, timestamp]]
        try:
            with open(self.filename[0], "a", newline="" ) as file:
                writer = csv.writer(file)
                writer.writerows(data_to_append)
        except AttributeError:
            self.clear_fields(self.name, self.title, self.department)
            self.table.setRowCount(0) # clears the table
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")
        except FileNotFoundError:
            self.clear_fields(self.name, self.title, self.department)
            self.table.setRowCount(0) # clears the table
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")

        self.clear_fields(self.name, self.title, self.department)

    def import_file(self):
        self.clear_fields(self.name, self.title, self.department)
        self.table.setRowCount(0) # clears the table
        self.filename = QFileDialog.getOpenFileName(self, 'create a new file', '', 'Data File (*.csv)',)
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            with open(self.filename[0], "r") as file:
                csvFile = csv.reader(file)
                next(csvFile) # skips the header

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
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['name', 'title', 'department', 'timestamp'])
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem('  '+name+'  '))
        self.table.setItem(row, 1, QTableWidgetItem('  '+title+'  '))
        self.table.setItem(row, 2, QTableWidgetItem('  '+department+'  '))
        self.table.setItem(row, 3, QTableWidgetItem('  '+timestamp+'  '))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def clear_fields(self, name, title, department):
            name.clear() 
            title.clear() 
            department.clear()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self):  # loads the About window
        self.about_window = AboutWindow(dark_mode=self.action_dark_mode.isChecked())
        self.about_window.show()

    def about_qt(self):  # loads the About Qt window
        QApplication.aboutQt()

    def closeEvent(self, event):  # Save settings when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()

class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.action_dark_mode.isChecked())

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
    