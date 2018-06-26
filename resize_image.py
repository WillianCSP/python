# import the necessary packages
#Criado para redimensionar um lote de imagens no tamanho desejado, imgem de 7 mb foi para 200 KB
 
import cv2
import os
import time

# load the image and show it
print("Inicio:"+time.ctime())
file_list = os.listdir("/home/adminuser/Pictures/grandes")
saved_path = os.getcwd()	
os.chdir("/home/adminuser/Pictures/grandes")
	
#para cada um, renomear
for file_name in file_list:
	os.chdir("/home/adminuser/Pictures/grandes")
	image = cv2.imread(file_name)
	print("Arquivo:"+file_name)
	#print image.shape
	r = 800.0 / image.shape[1] #Setando a largura calcula ja na proporcao correta o tamanho 
	dim = (800, int(image.shape[0] * r))
# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image	
# perform the actual resizing of the image and show it
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	#print("Arquivo MENOR:"+file_name)
	#print resized.shape
	os.chdir("/home/adminuser/Pictures/pequenas")
	cv2.imwrite(file_name, resized)
	#cv2.imshow("resized", resized)

print("Fim:"+time.ctime())
cv2.waitKey(0)

