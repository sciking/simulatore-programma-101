print """Emulatore delle funzioni del calcolatore
Olivetti P101. Sviluppato da Sciking
www.computerblog.ga - www.informatica-semplice.it"""
#piu informazioni presso http://computerblog.ga/2015/03/un-motore-per-emulare-la-perottina/
R = 0
B = 0
C = 0
D = 0
E = 0
F = 0
M = 0
A = 0
limite = 0
def regR(r):
	global R
	R = r
def regB(b):
	global B
	B = b
def regC(c):
	global C
	C = c
def regD(d):
	global D
	D = d
def regE(e):
	global E
	E = e
def regF(f):
	global F
	F = f
def regR(r):
	global R
	R = r
def regA(a):
	global A
	A = a
def immetti(m)
	global M
	M = m
       
def add(add2):
	global A
	global M
	A = A+add2
	print A
	return A
	M = add2
def sott(sott2):
	global A
	global M
	A = A-sott2
	print A
	return A
	M = sott2
def molt(molt2):
	global A
	global M
	A = A*molt2
	print A
	return A
	M = molt2
def div(div2):
	global A
	global M
	global R
	R = A%div2
	A = A/div2
	print A
	return A
	M = div2
def stampareg(reg):
	print reg
def ass(numero):
	global A
	A = abs(numero)
	print A
	return A
def esci():
	exit()
def carmagn(name):
	in_file = open(name,"r")
	text = in_file.read()
	in_file.close()
	exec text
def sqrt(reg):
	global A
	A = reg**0.5
	print A
def limitedecimali(limit):
	global limite
	if limit < 0 or limit > 16:
		print "Max 15!"
		menu()
	limite = limit
def limita():
	global A
	global M
	global R
	global B
	global C
	global D
	global E
	global limite
	global F
	round(A, limite)
	round(M, limite)
	round(R, limite)
	round(B, limite)
	round(C, limite)
	round(D, limite)
	round(E, limite)
	round(F, limite)
def immettidata(reg):
	global A
	global M
	global R
	global B
	global C
	global D
	global E
	global F
	registro = reg
	registro = input(">>")
	reg = registro
	#per ora non funziona.
def menu():
	input("Console P101/P203>>>  ")
	limita()
	menu()
       
menu()
#see more at http://computerblog.ga/2015/03/un-motore-per-emulare-la-perottina/
