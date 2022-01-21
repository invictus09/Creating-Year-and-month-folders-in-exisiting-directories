from pathlib import Path
import os

#Set the Path of Current directory
os.chdir('E:\Python New folder program')
Path.cwd()

#Check for All the Folder names in the existing diectory and only select and add to a new list where numbers are 4 Digits
AllFolders = (os.listdir())
parents = []
for folder in AllFolders:
    if len(folder) == 4:
        parents.append(folder)

#Define the Folders to add
print(parents)
years = ["2024"]
children = ["Mar 2024"]

#Code to run while we add new year
# for p in parents:
#     for y in years:
#         os.mkdir(os.path.join(p,y))

#Code to run while we add new month
for p in parents:
    for y in years:
        for c in children:
            os.mkdir(os.path.join(p,y,c))
          