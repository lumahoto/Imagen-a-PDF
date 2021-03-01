from PIL import Image															#Prueba de funciones
import tkinter as tk
import os


from tkinter import filedialog													# identificar carpeta base
root = tk.Tk()
root.withdraw()

carpeta_principal = filedialog.askdirectory()

carpetas = []

for root, dirs, files in os.walk(carpeta_principal):							#identificando archivos
	for file in files:
		if file.endswith('jpg'):
			if root in carpetas:
				continue
			else:
				carpetas.append(root)

for x in carpetas:																#creando lista de imágenes y convirtiendo a PDF
	imágenes = []
	for root, dirs, files in os.walk(x):
		for file in files:
			dirección = str(os.path.join(root, file))
			img = Image.open(dirección)
			img1 = img.convert('RGB')
			imágenes.append(img1)
	Archivo = str(x)+'.pdf'
	imágenes[0].save(Archivo,save_all=True, append_images=imágenes[1:])
print(carpetas)
print ('Listo.')
