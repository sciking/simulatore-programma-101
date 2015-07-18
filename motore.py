print """Emulatore delle funzioni dei calcolatori
Olivetti P101 e P103. Sviluppato da Sciking
www.computerblog.ga - www.informatica-semplice.it"""
#piu informazioni presso http://computerblog.ga/2015/03/un-motore-per-emulare-la-perottina/
K = 0
B = 0
C = 0
D = 0
E = 0
F = 0
M = 0
A = 0
def reg(k,b,c,d,e,f):
        global K
        global B
        global C
        global D
        global E
        global F
        K = k
        B = b
        C = c
        D = d
        E = e
        F = f
       
def add(add1,add2):
        global A
        global M
        A = add1+add2
        print A
        M = add2
def sott(sott1,sott2):
        global A
        global M
        A = sott1-sott2
        print A
        M = sott2
def molt(molt1,molt2):
        global A
        global M
        A = molt1*molt2
        print A
        M = molt2
def div(div1,div2):
        global A
        global M
        A = div1/div2
        print A
        M = div2
def stampanumero(num):
        print num
def stampareg(reg):
        print reg
def tekne(stringa):
        print stringa
def ass(numero):
        global A
        A = abs(numero)
        print A
def esci():
        exit()
def carmagn(name):
        in_file = open(name,"r")
        text = in_file.read()
        in_file.close()
        exec text
def sqrt(reg)
        global A
        A = reg**0.5
        print A
 
def menu():
        input("Console P101/P203>>>  ")
        menu()
       
menu()
#see more at http://computerblog.ga/2015/03/un-motore-per-emulare-la-perottina/
