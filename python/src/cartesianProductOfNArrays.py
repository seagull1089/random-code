#!/usr/bin/python 
'''
method to generate cartesian product of N arrays. 
'''

def iterArrays(prefix,queue_list,i): 
	if len(queue_list) > i  :
		current = queue_list[i]
		for x in current:
			for y in iterArrays(prefix + x, queue_list,i+1):
				yield y
	else:	
		yield  prefix

if __name__=="__main__":
	arr1 = ['a','b','c']
	arr2 = ['e','f','g','h'] 
	arr3 = ['i','j','k','l'] 
	queue_list = [ arr1,arr2,arr3]
	for x in iterArrays("",queue_list,0):
		print x 



