import functions as f

a = input("Digite el valor de 'a':")
b = input("Digite el valor de 'b':")

while (not (a.isdigit() and b.isdigit())):
	print("a y b deben ser valores numericos")
	a = input("Digite el valor de 'a':")
	b = input("Digite el valor de 'a':")
if (a > b):
	print("'a' debe ser menor que 'b'. Por lo tanto, 'a' será ", b,"y 'b' será ", a)
	temp = a
	a = b
	b = temp

a = int(a)
b = int(b)

f.punto1y2(a,b)