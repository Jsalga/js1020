Python 3.8.3rc1 (tags/v3.8.3rc1:802eb67, Apr 29 2020, 21:39:14) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum_divisors(n):
	sum = 0
	x = 1
	while n > x:
		if n % x == 0:
			sum += x
			x += 1
		else:
			x += 1
	return sum

>>> print(sum_divisors(36))
55
>>> 