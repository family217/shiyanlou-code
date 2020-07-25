for a in range(1,101):
	b = a % 7
	c = a % 10
	d = a // 10
	if b != 0 and c!=7 and d!=7:
		print(a)
