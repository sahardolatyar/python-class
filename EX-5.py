Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #kabise budan:
>>> def Julian_date (d, m , y):
	days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
	passed = 0
	if y%4==0 or (y%4==0 and y%100!=0):
		days[1]=29
	for months in days [:m-1]:
		passed+= months
	passed += d
	return passed

>>> #pos:
>>> def pos(n):
    for i in range(n+1):
            print (i)

            
>>> #baresiye bakhshpaziriye do adad bar ham
>>> def div (num1 , num2):
   if num2%num1==0 or num1%num2==0:
       return 'bakhsh pazir ast'
   else:
         return 'bakhsh pazir nist'

        
>>> #baresiye adad aval budan
>>> def prime (num):
    limit = int(num**0.5)
    for i in range(limit):
            if num %i == 0:
             return "aval nist"
    return "aval ast
SyntaxError: EOL while scanning string literal
>>> def prime (num):
    limit = int(num**0.5)
    for i in range(limit):
            if num %i == 0:
             return "aval nist"
    return "aval ast"

>>> 
