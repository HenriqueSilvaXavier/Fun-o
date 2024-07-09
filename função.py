x=int(input("Digite o valor de x: "))
f=input("Digite a função f(x): ")
if "!" not in f:
	y=eval(f.replace("x", str(x)))
if "!" in f:
	f2=f
	while "!" in f2:
		y=1
		c=x
		f2=f2.replace("x", str(x))
		while "(" and ")" in f2:
			i3=f2.find("(")
			i4=f2.find(")")
			n2=eval(f2[(i3+1):(i4)])
			lista=[]
			for k in f2:
				lista.append(k)
			f2=""
			del lista[i3:(i4+1)]
			lista.insert(i3, str(n2))
			for k in lista:
				f2=f2+k
		i=f2.find("!")
		if f2[i-1].isnumeric()==True:
			i2=1
			n=f2[i-1]
			while f2[i-i2].isnumeric()==True and i-i2>=1:
				i2=i2+1
				n=f2[i-i2]+n
			c=int(n)
			while c>=1:
				y=y*c
				c=c-1
		while c>=1:
			y=y*c
			c=c-1
		y=str(y)
		s=n+"!"
		f2=f2.replace(s, y)
	y=eval(f2)
print("O valor de f(x) para x =", x, "é", y)
