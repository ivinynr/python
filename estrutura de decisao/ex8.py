qtatual= 205
qtmax= 500
qtmin= 100
qtmed= float


qtatual=("informe a quantidade atual em estoque: ", str (205))
qtmax=("informe a quantidade máxima em estoque: ", str (500))
qtmin=("informe a quantidade minima em estoque: ", str  (100))

qtmed= (qtmax + qtmin) /2
print(f'sua media é:{qtmed}')

if (qtmed >= qtatual): 
    print("Quantidade média =",qtmed,".Não efetuar compra!")

else:

    print("Quantidade média =",qtmed,".Efetuar compra!")





