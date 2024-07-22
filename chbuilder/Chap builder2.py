from Chapbuilder import *
import os

#specify at folder_path end where to create files --> Chapter 8 would be changed to Chapter 9 and so forth after Chapter folder is created
folder_path = 'c:\\Users\\Fayed\\boot.dev\\Python course tests\\Chapter 8'
chapter = ""

#Sets Array/list to selected amount of generations. code can be changed to user input as well
# --> int(input()) and then contents_ch(name_of_input_var)
myList = contents_ch(3)

#This can be altered. Ideally create a loop that creates amount of 'file openings' 
#it would need to change myList index, assign it to chapter variable. And then update the file path each time. 
#Lastly execute the file generations
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

#Goal for the finished chapter generator, is to input a number. For example 10 in console.
#Code would then execute, and create 10 chapters, each chapter has a corresponding chapter for the main
#Hence creating 20 files, numerized in order. 
#Also create files for challenges. This should be pretty simple

#in V2.0 It should let me select the name for each chapter, then gererate. i.e if i want chapters for 1-7 and then 10-13
