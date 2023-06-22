#To avoid paddlepaddle duplication
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

#lib imports
from PIL import Image
import cv2 as cv
import re
import json
from paddleocr import PaddleOCR,draw_ocr

#Path to images
#img_path = 'ex5.jpg' #CNH 2022
img_path = '1.png' #NOME TESTE CENTO E DEZ - CNH 2022

#Reading, resizing, grayscale and declaring ocr
img = cv.imread(img_path)
resizing = cv.resize(img, (1100, 700))
img_gray = cv.cvtColor(resizing, cv.COLOR_BGR2GRAY)
img_bw = cv.threshold(img_gray, 143.5, 220, cv.THRESH_BINARY)[1]
ocr = PaddleOCR(debug=False, show_log = False)

#Using already trained cascade classifier
face_classifier = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Creating a directory to save CNH info and pictures
os.makedirs("CNH_Data", exist_ok=True)

#Detecting face with opencv
faces = face_classifier.detectMultiScale(img_bw, 1.1, 5)

#Bounding box around Area of interest - face
for(xf,yf,wf,hf) in faces:
    cv.rectangle(resizing, (xf,yf), (xf+wf, yf+hf), (0,0,255),2)

#Area of interest - Birthday cropping
x, y, w, h = 450, 245, 650, 40
img_c = resizing[y:y+h, x:x+w]
#Applying threshold
img_bw1 = cv.threshold(img_c, 143.5, 220, cv.THRESH_BINARY)[1]

#Area of interest - Birthday bounding box
cv.rectangle(resizing, (x, y), (x+w, y+h), (255,0,0), 2)

#Area of interest - Name cropping
a, b, c, d = 185, 200, 1100, 50
img_a = img_gray[b:b+d, a:a+c]
#Applying threshold
img_bw2 = cv.threshold(img_a, 130, 220, cv.THRESH_BINARY)[1] 

#Area of interest - Name's bounding box
cv.rectangle(resizing, (a, b), (a+c, b+d), (255,0,0), 2)

#Area of interest - Expiration cropping
xe, ye, we, he = 450, 290, 650, 60
img_y = resizing[ye:ye+he, xe:xe+we]
#Applying threshold
img_bw3 = cv.threshold(img_y, 143.5, 220, cv.THRESH_BINARY)[1]

#Area of interest - Expiration bounding box
cv.rectangle(resizing, (xe, ye), (xe+we, ye+he), (255,0,0), 2)

#Area of interest - CPF/category cropping
xc, yc, wc, hc = 450, 400, 650, 60
img_cpf = resizing[yc:yc+hc, xc:xc+wc]
#Applying threshold
img_bw4 = cv.threshold(img_cpf, 143.5, 220, cv.THRESH_BINARY)[1]

#Area of interest - CPF/category bounding box
cv.rectangle(resizing, (xc, yc), (xc+wc, yc+hc), (255,0,0), 2)

#Birth output
birthresult = ocr.ocr(img_c, cls=True)
for idx in range(len(birthresult)):
    res = birthresult[idx]

#19/09/1981SAOPAULO/SP
def split_bday(data):
    splitted = data.split("/")
    day = splitted[0]
    month = splitted[1]
    year = splitted[2][0:4]
    city = splitted[2][4:]
    uf = splitted[3]

    return f"{day}/{month}/{year}", f"{city}/{uf}"

#Filtered birthdate from tuple
bday_tuple = res[0][1]
cnh_bday = bday_tuple[0]
bday, location = split_bday(cnh_bday)



#Name output
resulting = ocr.ocr(img_bw2, cls=True)
for i in range(len(resulting)):
    r = resulting[i]

#Filtered name from tuple
filt = list(r)  
name_tuple = r[0][1]
cnh_name = name_tuple[0]

#Expiration output 
expresult = ocr.ocr(img_y, cls=True)
for idx_e in range(len(expresult)):
    res_e = expresult[idx]

#Filtered expiration date from tuple
e_filter = res_e[len(res_e)-1]
exp_tuple = e_filter[len(e_filter)-1]
cnh_expiration = exp_tuple[0]

#CPF/category output
cpfresult = ocr.ocr(img_cpf, cls=True)
for idx_c in range(len(cpfresult)):
    res_c = cpfresult[idx_c]

#Filtered category from tuple
cat_filter = res_c[len(res_c)-1]
cat_tuple = cat_filter[len(cat_filter)-1]
cnh_category = cat_tuple[0]

#Filtered cpf - might try regex later
cpf_index = res_c[3]
cpf_tuple = cpf_index[1]
cnh_cpf = cpf_tuple[0]

"""#Writing JSON file
cnh_json = { 'id': 1,
             'Nome': cnh_name, 
             'Aniversario_e_UF': cnh_bday, 
             'CPF': cnh_cpf, 
             'Categoria': cnh_category, 
             'Validade': cnh_expiration
            },

#Creating the JSON file
with open ("CNH_Data/cnh_info.json", "w") as arquivo:
    json.dump(cnh_json, arquivo, indent = 4)

imgfilename = f'Face({1}).jpg'
savingimg = 'CNH_Data/' + imgfilename
#Saving face inside the recently created directory
cnh_face = resizing[yf:yf+hf, xf:xf+wf]
cv.imwrite(savingimg, cnh_face)"""

#Loading JSON file before writing on it
with open("CNH_Data/cnh_info.json", "r") as arquivo:
    data = json.load(arquivo)

#Verifica comprimento da lista existente e realiza autoincremento
id = len(data)+1

#Nova entrada na lista
new_cnh_entry = {'id': id,
                 'Nome': cnh_name, 
                 'Aniversario': bday, 
                 'Localidade': location,
                 'CPF': cnh_cpf, 
                 'Categoria': cnh_category, 
                 'Validade': cnh_expiration
                }
#Append da lista já existente e a nova entrada
data.append(new_cnh_entry)

id_img = id
imgfilename = f'Face({id_img}).jpg'
savingimg = 'CNH_Data/' + imgfilename

#Saving face inside the recently created directory
cnh_face = resizing[yf:yf+hf, xf:xf+wf]
cv.imwrite(savingimg, cnh_face)

#Autoincremento
id +=1

#Atualizando o JSON
with open("CNH_Data/cnh_info.json" , "w") as arquivo:
    json.dump(data, arquivo, indent= 4)

#Showing bounding boxes on image of choice
cv.imshow('imagem', resizing)
cv.waitKey(0)
cv.destroyAllWindows() 