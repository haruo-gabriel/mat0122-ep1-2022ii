from factoring_support import intsqrt
from math import sqrt

def root_method(N):
	"""
	input: an integer N
	output: an integer y such that y*y is close to N and, if N happens to be a perfect square, y*y is exactly N
	"""
	a = intsqrt(N)+1
	#for i in range(10):
	while True:
		#print(f"a = {a}")
		b = intsqrt(a**2 - N)
		#print(f"b = {b}")
		if(b *b == x):
			#print(f"a - b = {a-b}")
			return int(a - b)
		else:
			a += 1

if __name__ == "__main__":
	print(root_method(146771))