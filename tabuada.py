# numero = int(input("Digite o número\n"))

# for i in range(1,11):
#   print(f"{numero} x {i} = {numero*i}")



def mesclar(esquerda,direita):
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado