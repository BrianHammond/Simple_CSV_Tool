from class_csv import *
import os
menu = ("""
1. Write a new file      
2. Append file
3. Read File
0. Exit  
""")

csv_folder = input("folder: ")
csv_file = input("file: ") + ".csv"
csv_full_path = csv_folder +  "/" + csv_file

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0 :
            break

        case 1:
            if not os.path.isdir(csv_folder):
                print(f"{csv_folder} not found, creating folder")
                os.makedirs(csv_folder)
                Write_Append(csv_folder, csv_file).write()

        case 2:
            Write_Append(csv_folder, csv_file).append()

        case 3:
            if not os.path.isfile(csv_full_path):
                print(f"{csv_full_path} not found, try again")
            else:
                Read_CSV(csv_folder, csv_file).read()
    
        case _:
            print ("pick a valid option")