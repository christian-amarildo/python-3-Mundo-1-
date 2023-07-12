import math
grau = int(input("insira o grau: "))
cosseno = math.cos(math.radians(grau))
seno = math.sin(math.radians(grau))
tangente = math.tan(math.radians(grau))
print("o seno, o cosseno e a tangente do grau {} é {} , {} e {}".format(grau,seno,cosseno,tangente))
