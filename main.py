from class_csv import *

menu = ("""
1. Write a new file      
2. Append file (will overwrite existing file)
0. Exit  
""")

folder = input("folder: ")
file = input("file: ") + ".csv"

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0 :
            break

        case 1:
            Folder(folder, file).check()
            Information(folder, file).write()

        case 2:
            Information(folder, file).append()
    
        case _:
            print ("pick a valid option")