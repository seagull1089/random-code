#!/usr/bin/python 
import random
import string
'''
method to generate random strings from ascii characters and digits. 
'''

def generateRandomString(length = 32 , chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(length))

if __name__=="__main__":
	for i in xrange(0,100):
		print generateRandomString(100)
	
