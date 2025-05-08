nombre= input("¿Como te llamas? ")
print("Hola," , nombre)

strEdad = input("¿Cuantos años tienes? ")
strAnno = input("¿En que año estamos? ")
strMes = input("¿En que mes estamos? ")
strDia = input("¿En que dia estamos? ")

edad = int(strEdad)
anno = int(strAnno)
mes = int(strMes)
dia = int(strDia)

""" meses"""
mes1 =31
mes2=28
mes3=31
mes4=30
mes5031
mes6=30
mes7=31
mes8=31
mes9=30
mes10=31
mes11=30
mes12=31

if mes == 1:
     transcurridos = dia
if mes == 2:
     transcurridos = mes1 + dia
if mes == 3:
     transcurridos = mes1 + mes2 + dia
if mes == 4:
     transcurridos = mes1 + mes2 + mes3 +dia
if mes == 5:
     transcurridos = mes1 + mes2 + mes3  + mes4 +dia
if mes == 6:
     transcurridos = 31 + 28 + 31 +31 + 30 +dia
if mes == 7:
     transcurridos = 31 + 28 + 31 +31 + 30 +31 +dia
if mes == 8:
     transcurridos = 31 + 28 + 31 +31 + 30 +31 + 31 +dia
if mes == 9:
     transcurridos = 31 + 28 + 31 +31 + 30 +31 + 31 + 30 +dia
if mes == 10:
     transcurridos = 31 + 28 + 31 +31 + 30 +31 + 31 + 30 + 31 +dia
if mes == 11:
     transcurridos = 31 + 28 + 31 +31 + 30 +31 + 31 + 30 +31 + 30 +dia
if mes == 12:
     transcurridos = 31 + 28 + 31 +31 + 30 +31 + 31 + 30 +31 + 30 + 31+ dia

prob = transcurridos /365*100
nacimiento = anno - edad

print(npmbre, "naciste en", nacimiento, "con una probabilidad de",prob)
print"o en", nacimiento -1, "con una probabilidad de, 100- prob)

