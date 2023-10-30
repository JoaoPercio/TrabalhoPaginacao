# taking arguments from cmd and saving in a array
from sys import argv
import math

endereco_virtual= int(argv[1])

tamanho_pag = 4096
num_bits = 16

num_bits_deslocamento= int(math.log(tamanho_pag,2))

# calcula o numero de bits para pagina
num_bits_pagina = num_bits - num_bits_deslocamento

mascara_deslocamento =(1<< num_bits_deslocamento) -1 #mascara de 12 bits com bits em 1
num_deslocamento = endereco_virtual & mascara_deslocamento #bit a bit com a mascara para descobrir o deslocamento

mascara_pagina= ((1<< num_bits_pagina) -1) << num_bits_deslocamento #mascara de bits com 4 bits em 1, 4 primeiro bits deslocados
num_pagina= (endereco_virtual & mascara_pagina) >> num_bits_deslocamento #bit a bit com a mascara para descobrir o numero de paginas, e deslocar de volta os 4 bits

print("endereço virtual passado:" ,endereco_virtual)
print("número de página: ",num_pagina)
print("deslocamento: ",num_deslocamento)

# posicao - 1 para considerar a primeira linha do arquivo como 0
posicao = num_pagina * tamanho_pag + num_deslocamento - 1
f= open('data_memory.txt', 'r')
content = f.readlines()
print("Valor: ", content[posicao])
f.close()