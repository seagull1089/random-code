#!/usr/bin/python 
'''
 cool memoizing stuff in python. 
 using annotation before methods is pretty cool in scripting. 
'''
def memoize(f):
	cache = {}
	def helper(x):
		if not x in cache:
			cache[x] = f(x) 
			print "\t\t computing for %d" %(x)
		return cache[x]
	return helper	
@memoize
def factorial(n):
	if n ==0 or n ==1 :
		return 1
	else:
		return n*factorial(n-1)
@memoize
def fib(n):
	if n == 0 or n ==1: 
		return 1
	else:
		return fib(n-1) + fib(n-2)

if __name__=="__main__":
	for i in range(0,100,10):
		print "Fibonacci %d  = %d " %(i,fib(i))
		print "Factorial %d  = %d " %(i,factorial(i))
