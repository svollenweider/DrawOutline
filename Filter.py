import numpy as np

Tofilter = np.array([False,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False])

def filter(input,minsize=5):
	counter = 0
	for i in range(len(input)):
		if not input[i]:
			if counter==0:
				continue
			if counter<minsize:
				input[i-counter:i] = False
				counter=0
			if counter>minsize:
				counter=0
		else:
			counter +=1
	if counter != 0 and counter<maxsize:
		input[-counter:] = False
	return input
				
				