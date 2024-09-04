
s = input("Πληκτρολογήστε ένα αλφαριθμητικό: ")

if len(s) == 1:
    print('Μήκος = 1')
else:
   
    if s == s[::-1]:
       
        adict = {s: len(s)}
        print(adict)
        
        
        alist = list(s)
        print(alist)
    else:
        print('Δεν είναι παλίνδρομο')