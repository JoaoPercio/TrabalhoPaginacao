from sys import argv
import math



endereco_virtual= int(argv[1])
print("endereco virtual:", hex(endereco_virtual))
tamanho_pag = 4096
num_bits_deslocamento = 0
num_bits = 32
m=11
f= open('addresses_32b.txt', 'r')
content= f.readlines()



num_bits_deslocamento= int(math.log(tamanho_pag,2))
hash= endereco_virtual%m


deslocamento = 0xfff & endereco_virtual #offset
print("deslocamento: ", hex(deslocamento))


posicao= hash * tamanho_pag + deslocamento

print(hex(posicao))
f= open('data_memory.txt', 'r')
content = f.readlines()
print(content[posicao])
f.close()


