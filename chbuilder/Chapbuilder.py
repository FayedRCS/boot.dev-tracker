        #function to take in an amount of chapter files to create
def contents_ch(num):
   starting = 0
   ch = 1
   sec = 9
   myList = []
   
   #appends amount input to myList, and changes the name of the .py file accordingly
   while starting < num:
      myList.append(f"ch{sec}{ch}.py")
      ch += 1
      starting += 1
   
   #returning myList only
   
   return myList

print(contents_ch(3))
   #Fields of improvements here: 
   #Create a copy of each python file, and put a char = "m", at the end, but before .py
   #So that the list created looks like this : [ch1.py, ch1m.py, ch2.py, ch2m.py] etc.
   #Conditions need to be specified