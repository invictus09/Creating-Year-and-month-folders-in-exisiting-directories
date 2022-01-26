from pathlib import Path
import os
import datetime

#Set the Path of Current directory
os.chdir(r'E:\Python_NewFolder')
Path.cwd()

#Check for All the Folder names in the existing diectory and only select and add to a new list where folder length is equal to 4
AllFolders = (os.listdir())
parents = []
for folder in AllFolders:
    if len(folder) == 4:
        parents.append(folder)

#Define the Folders to add
print(parents)
current_year = datetime.datetime.now().strftime("%Y")
current_month = datetime.datetime.now().strftime("%B") + '_' + current_year

# Creating sub-folders recursively
for p in parents:
    try:
        os.mkdir(os.path.join(p,current_year))
        os.mkdir(os.path.join(p,current_year,current_month))
    except FileExistsError as e:
        print("All sub-folders already exist", os.path.join(p,current_year,current_month))