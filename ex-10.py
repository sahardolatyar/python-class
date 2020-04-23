Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class coordinate:
	x=0
	y=0

	
>>> p1=coordinate()
>>> p2=coordinate()
>>> p1.x=3
>>> p1.y=4
>>> p2.x=10
>>> p2.y=7
>>> def func1(p1 , p2):
return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
func1(p1, p2)
