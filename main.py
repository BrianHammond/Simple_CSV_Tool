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
        self.button_add.clicked.connect(self.add_info)
        self.button_update.clicked.connect(self.update_info)
        self.button_delete.clicked.connect(self.delete_row)

        #menu bar
        self.action_new.triggered.connect(self.new_file)
        self.action_open.triggered.connect(self.open_file)
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)

        # text fields
        self.name = self.line_name
        self.title = self.line_title
        self.department = self.line_department

    def new_file(self):
        self.initialize_table()
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

    def open_file(self):
        self.initialize_table()
        self.filename = QFileDialog.getOpenFileName(self, 'Open file', '', 'Data File (*.csv)',)

        if not self.filename[0]:
            return  # Do nothing if no file is selected
        
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

    def add_info(self):
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

    def update_info(self):
        # Get the updated values from the table
        rows = self.table.rowCount()
        columns = self.table.columnCount()

        # Check if the table has rows and columns
        if rows == 0 or columns == 0:
            QMessageBox.warning(self, "Empty Table", "The table is empty. Please add some data first.")
            return

        # Prepare the updated data
        updated_data = []

        for row in range(rows):
            row_data = []
            for col in range(columns):
                # Get the new value from the table cell
                item = self.table.item(row, col)
                if item is not None:
                    row_data.append(item.text())  # Append the edited text from the cell
                else:
                    row_data.append('')  # If the cell is empty, append an empty string
            updated_data.append(row_data)

        # Write the updated data back to the CSV file
        try:
            with open(self.filename[0], "r") as file:
                csvFile = csv.reader(file)
                existing_data = list(csvFile)  # Read all existing data (including header)

            # Replace the data part with the updated data (skip the header row)
            updated_data_with_header = [existing_data[0]] + updated_data  # Include the header in the updated data

            # Write the updated data back to the CSV file
            with open(self.filename[0], "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data_with_header)

            # Optionally, you could update the table immediately after writing to the CSV, but it's already in sync.
            QMessageBox.information(self, "Update Successful", "The table data has been updated in the CSV file.")
            
        except FileNotFoundError:
            QMessageBox.warning(self, "File Not Found", "Please select or create a file first.")
        
        self.table.resizeColumnsToContents()

    def delete_row(self):
        current_row = self.table.currentRow()
        
        if current_row >= 0:
            # Remove the row from the table
            self.table.removeRow(current_row)
            
            # Now, we will update the CSV file by removing the corresponding row
            try:
                with open(self.filename[0], "r") as file:
                    csvFile = csv.reader(file)
                    existing_data = list(csvFile)  # Read all data

                # Remove the row to delete (skip header)
                updated_data = [row for i, row in enumerate(existing_data) if i != current_row + 1]

                # Write the updated data back to the CSV file
                with open(self.filename[0], "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(updated_data)

                QMessageBox.information(self, "Delete Successful", "The selected row has been deleted.")
            
            except FileNotFoundError:
                QMessageBox.warning(self, "File Not Found", "Please select or create a file first.")
        else:
            QMessageBox.warning(self, "No Row Selected", "Please select a row to delete.")

    def initialize_table(self):
        self.table.setRowCount(0) # clears the table
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['name', 'title', 'department', 'timestamp'])

    def populate_table(self, row, name, title, department, timestamp):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(title))
        self.table.setItem(row, 2, QTableWidgetItem(department))
        self.table.setItem(row, 3, QTableWidgetItem(timestamp))
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
    