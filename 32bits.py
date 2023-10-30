from sys import argv
import math

endereco_virtual= int(argv[1])

tamanho_pag = 4096
num_bits = 32

num_bits_deslocamento= int(math.log(tamanho_pag,2)) #calcular  a quantidade de bits de deslocamento

0x3ff # mascara de 10 bits
p2= ((0x3ff << num_bits_deslocamento) & endereco_virtual) >> num_bits_deslocamento # pegar os 10 bits do meio 
p1=((0x3ff << (num_bits_deslocamento+10)) & endereco_virtual) >> (num_bits_deslocamento+10) # +10 para pegar os bits mais a esquerda

mascara_deslocamento = (1<< num_bits_deslocamento) -1 #mascara de 12 bits com bits em 1
deslocamento =  endereco_virtual & mascara_deslocamento #offset

print("número pagina 1: ",p1)
print("número pagina 2: ",p2)
print("deslocamento: ",deslocamento)

posicao = (p1 * 1024 * tamanho_pag) + (p2 * tamanho_pag) + deslocamento -1
f= open('data_memory.txt', 'r')
content = f.readlines()
print("valor: ",content[posicao])
f.close()


