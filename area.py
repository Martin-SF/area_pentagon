import numpy as np

e = 5 #number of corners
b0 = np.sqrt(4*1/np.sqrt(25+10*np.sqrt(5))) 

# area=1 for this values: 
#b0 = np.sqrt(2)
#b0 = np.sqrt(2/(np.sqrt(27))) 6eck

phi = np.pi*(1-(2/e))
alpha = (np.pi-phi)/2
gamma = np.sqrt(2*(1-np.cos(phi)))

Pc = gamma-2*1/gamma

def part_area_pentagon(j):
	b = b0*(Pc**j)
	
	c = b*gamma
	d = b*1/gamma
	
	return e*1/2*(np.sin(alpha)*b*d+(c-2*d)*np.sin(phi)*d)

values = []
area = 0
for i in range(0, 100):
  values.append(part_area_pentagon(i))
  area += values[i]
  

np.sum(values)  #no output!?!

print(lol)

















