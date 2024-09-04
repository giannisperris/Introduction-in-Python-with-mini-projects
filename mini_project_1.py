a1 = float(input('a1 = '))
a2 = float(input('a2 = '))
b1 = float(input('b1 = '))
b2 = float(input('b2 = '))

import math 


ab = (a1*b1) + (a2*b2)

a = math.sqrt(a1**2 + a2**2)
b = math.sqrt(b1**2 + b2**2)

costh = math.cos((ab)/(a*b))
goniath = math.degrees(costh)

print("costh : ",costh , "goniath : " , goniath)










