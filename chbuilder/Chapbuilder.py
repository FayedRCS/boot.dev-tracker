def contents_ch(num):
   starting = 0
   ch = 81
   myList = []
   
   while starting < num:
      myList.append(f"ch{ch}.py")
      ch += 1
      starting += 1
   
      
      
   
   return myList
   
print(contents_ch(3))