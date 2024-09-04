while True:
     year = input("Εισάγετε τη χρονολογία ή 'q' για έξοδο: ")
     
     if year == 'q':
         break 
     
     year = int(year)

     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
         disekto = True
     else:
         disekto = False
      

     print(disekto)

print('Τέλος προγράμματος')
