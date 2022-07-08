frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    # Vai pegar o numero de letras, o menos 1 é pq começa do zero, então se tem 20 letras, vai do 0 ao 19.
    # Vai até a letra -1, que é antes da primeira, e vai voltando uma letra
    # Se a frase ao contrário for igual a ela mesma, ela é um palindromo
    inverso += junto[letra]
print('O inverso de {}, é {}.'.format(junto, inverso))
if junto == inverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

#Sem o for: invers == junto[::-1], pega do inicio ao fim, de trás pra frente, sem precisar do for.