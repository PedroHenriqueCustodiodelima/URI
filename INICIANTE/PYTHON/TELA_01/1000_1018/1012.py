atividade = input().split()
a = float(atividade[0])
b = float(atividade[1])
c = float(atividade[2])
calculo1 = a*c/2
calculo2 = 3.14159* (c*c)
calculo3 = (a+b)*c/2
calculo4 = b*b
calculo5 = a*b
print("TRIANGULO: {:.3f}".format(calculo1))
print("CIRCULO: {:.3f}".format(calculo2))
print("TRAPEZIO: {:.3f}".format(calculo3))
print("QUADRADO: {:.3f}".format(calculo4))
print("RETANGULO: {:.3f}".format(calculo5))