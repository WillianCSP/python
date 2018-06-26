#Renomeia arquivos, retirando numeros 0123456789

import os

def rename_files():
	#pegar arquivos
	file_list = os.listdir("/home/adminuser/Pictures")	
	print(file_list)
	saved_path = os.getcwd()
	print("Diretorio atual: "+saved_path)	
	os.chdir("/home/adminuser/Pictures")	
	#para cada um, renomear
	for file_name in file_list:
		print("Nome antigo:"+file_name)
		print("Nome novo:"+file_name.translate(None, "0123456789"))
		os.rename(file_name,file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
	
rename_files()
