#!/usr/bin/python 
from collections import deque 
'''
Given the number of quarters available, 
		the number of dimes available, 
		and number of 5 cent coins available, 

	return the the change for a given value in the available denominations. 
	change for less than 5 cents can be ignored. 
uses breadth first search to generate change. 
'''
def getSum(item): 
	return item[0]*25 + item[1]*10 + item[2]*5;

def getChange(cents,quarters,dimes,nickels):
	start = [0,0,0] 
	queue = deque([ start ])	
	while(len(queue)  >  0): 
		item = queue.popleft()
		if getSum(item) > cents: 
			continue
		if cents - getSum(item) < 5: 
			return item
		if quarters - item[0] > 0 : 
			x = item[:] 
			x[0] += 1
			queue.append(x)
		if dimes - item[1] >0: 
			x = item[:]
			x[1] += 1
			queue.append(x)	
		if nickels - item[2] > 0: 
			x = item[:]
			x[2] += 1 
			queue.append(x)
	raise Exception('no change','get lost')


if __name__ =="__main__": 
	print getChange(65,1,2,4)
