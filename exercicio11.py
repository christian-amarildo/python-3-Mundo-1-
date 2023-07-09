largura = int(input("insira a largura da parede: "))
altura = int(input("insita a altura da parede: "))
area = altura * largura
tinta = area // 2
if area % 2 != 0 :
    tinta = tinta + 1
print("largura: ", largura)
print("altura: ", altura)
print("area: ", area)
print("litros de tinta necessário: ",tinta)