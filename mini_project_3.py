x = int(input('x = '))
y = int(input('y = '))

list = [x*i for i in range(1,y+1) ]

print('list :' , list)

mylist_p = []
mylist_a = []
mylist01 = []

for mylist01 in list:
     if mylist01 % 2 == 0:
        print(0, 'είναι άρτιος αριθμός')
     else:
        print(1 ,'είναι περιττός αριθμός')

for a in list:
   if a % 2 == 0:
      mylist_p.append(a)
   else: 
      mylist_a.append(a)      
print('mylist_p :' , mylist_p)
print('mylist_a :' , mylist_a)