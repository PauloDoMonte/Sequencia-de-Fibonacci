def fib(n):
	a = 0
	b = 1
	while(b < n):
		c = a
		a = b
		b = a + c
		print(a)

n = int(input("Digite até que n quer a sequencia: "))
fib(n)
