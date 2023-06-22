import numpy as np
import cv2 as cv
#import pytesseract 

# Giving a name to the file
files = '1.png'

# Tesseract-OCR PATH
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#OpenCV reading file
img = cv.imread(files)
resizing = cv.resize(img, (1100, 700))
img_gray = cv.cvtColor(resizing, cv.COLOR_BGR2GRAY)

"""#Testing
x, y, w, h = 450, 235, 650, 145
img_c = img_gray[y:y+h, x:x+w]
img_test = cv.threshold(img_c, 143.5, 220, cv.THRESH_BINARY)[1]"""


#Cropping image 1
x, y, w, h = 185, 190, 1100, 50
img_crop = img_gray[y:y+h, x:x+w]
#Applying threshold
img_bw = cv.threshold(img_crop, 143.5, 220, cv.THRESH_BINARY)[1]

"""
#Cropping 2

#these values are good: 350, 400, 600, 400
a, b, c, d = 350, 400, 600, 400
img_crop2 = img_gray[b:b+d, a:a+c]"""
#Applying threshold
#img_bw2 = cv.threshold(img_crop2, 144.5, 220, cv.THRESH_BINARY)[1]

"""#subcrop_docidentidade
l, g, r, k = 140, 50, 500, 50
img_subcrop = img_bw2[g:g+k, l:l+r]"""

#subcrop_cpf
#v, s, t, q = 140, 100, 180, 50
#img_subcrop2 = img_bw2[s:s+q, v:v+t]

"""#subcrop_nregistro -- provavelmente n vou precisar
j, m, n, o = 350, 100, 180, 50
img_subcrop3 = img_bw2[m:m+o, j:j+n]"""

#categoria
#e, f, i, p = 890, 510, 100, 40
#img_subcrop4 = img_gray[f:f+p, e:e+i]
#Applying threshold
#img_bw3 = cv.threshold(img_subcrop4, 140.5, 220, cv.THRESH_BINARY)[1]

#Tesseract config
#config = ('-l por --oem 1 --psm 3')


#subcrop too, but it probably won't work

#Reading image text 
#text = pytesseract.image_to_string(img_bw, config=config) #Nome
#text2 = pytesseract.image_to_string(img_bw2, config=config)

"""#subcrop doc. identidade
subtext = pytesseract.image_to_string(img_subcrop, config=config)"""

#subcrop cpf
#subcpf = pytesseract.image_to_string(img_subcrop2, config = config)

"""#subcrop n. registro - provavelmente n vou precisar
subnreg = pytesseract.image_to_string(img_subcrop3, config = config)"""

#subcrop categoria
#subcat = pytesseract.image_to_string(img_subcrop4, config=config)

#Nome/Sobrenome
#print(text)

##Restante dos dados
#print(text2)

#Subcrops
#print(subtext)

#print(subcpf.split()[2])

#print(subnreg.split()[4]) -- pode ser q n precise

#print(subcat)

#testing
#cv.imshow('Imagem', img_test)


cv.imshow('Imagem', img_bw)
#cv.imshow('Imagem2', img_bw2)
#cv.imshow('SubImagem', img_subcrop)
#cv.imshow('SubImagem2', img_subcrop2)
#cv.imshow('SubImagem3', img_subcrop3)
#cv.imshow('SubImagem4', img_bw3)
cv.waitKey(0)
cv.destroyAllWindows() 


"""CPF tem padrão definido. É composto por onze dígitos numéricos, 
sendo os dois últimos dígitos verificadores.

O nº de registro tbm tem o padrão de 11 dígitos

Existem 5 tipos de categoria de CNH - A, B, C, D e E"""

"""Só preciso extrair as seguintes informações:

-Foto
-Nome (ja tenh)
-CPF (ja tenh)
-Data de Nascimento 
-categoria
-data de validade"""
