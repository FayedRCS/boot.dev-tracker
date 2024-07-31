def filter_messages(messages):
   #final list results of what we want to return
   instances = [] 
   final_msg = []

   #loop thorugh each index in messages

   for message in messages:
      counter = 0
      filtered = []
      #loops through each word, split by .split() method

      for dang in message.split():
         if dang == "dang":
            counter += 1
            
            #Alternate way: 
         #else:
            #filtered.append(dang)


      #loop through the messages, appending each word that isn't "dang"
      for word in message.split():
         if word != "dang":
            filtered.append(word)

         
      #appending the joined (by whitespace) words, into final list
      final_msg.append(" ".join(filtered))
      #appending each tally into a list
      instances.append(counter)


   return final_msg, instances


#Why does the funciton only work when in an array? or as several strings?
test = ["dang how's it going boy?"]
print(filter_messages(test))