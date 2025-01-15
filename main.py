from class_csv import *

menu = ("""
1. Write a new file      
2. Append file
3. Read File
0. Exit  
""")

csv_folder = input("folder: ")
csv_file = input("file: ") + ".csv"

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0 :
            break

        case 1:
            Folder(csv_folder, csv_file).check()
            Write_Append(csv_folder, csv_file).write()

        case 2:
            Write_Append(csv_folder, csv_file).append()

        case 3:
            Read_CSV(csv_folder, csv_file).read()
    
        case _:
            print ("pick a valid option")