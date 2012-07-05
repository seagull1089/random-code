#!/usr/bin/python 
'''
A method to generate all subsets from a given list in a iterative
fashion. iterate from 1 to 2^n and for each number, use the binary representation 
of the number to decide which element to display. 	
''' 
def generateAllSubsets(list): 
	for i in xrange(1,2**len(list)): 
		count = 0
		while i>0:
			if i%2 > 0: 
				print list[count],
			i=i/2
			count += 1
		print ""
 
if __name__=="__main__": 
	generateAllSubsets("abc")			
	
