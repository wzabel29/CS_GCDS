#1-'bring an umbrella just in case'

""" musicians = ['Tame Impala', 'Disclosure', 'MGMT']                   #2
musicians.insert(3, 'Katy Perry')
print(musicians[1])
musicians.pop(0)
print(musicians)
 """
#3-prints either a, b, or c twice

import random
i = 0
	
while i < 3:
	print(i, random.choice(["a", "b", "c"]))
	i += 1