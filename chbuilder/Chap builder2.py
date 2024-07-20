from Chapbuilder import *
import os

folder_path = 'c:\\Users\\Fayed\\boot.dev\\Python course tests\\Chapter 8'
chapter = ""


myList = contents_ch(3)

chapter = myList[0]
file_path = os.path.join(folder_path, chapter)
with open(file_path, 'w') as chBuilt:
    pass

chapter = myList[1]
file_path = os.path.join(folder_path, chapter)
with open(file_path, 'w') as chBuilt:
    pass

chapter = myList[2]
file_path = os.path.join(folder_path, chapter)
with open(file_path, 'w') as chBuilt:
    pass

