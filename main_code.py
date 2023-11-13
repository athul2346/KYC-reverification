import os
import sys
import cx_Oracle
import cv2
import numpy as np
import imutils
import pytesseract
import PIL
from PIL import Image
import xlsxwriter
from new_vision_test import func
import os
import re
import face_recognition
from datetime import date, datetime
import io

today = date.today()
imagePath='F:\\my code\\reverification\\input'
realinput="F:\\my code\\reverification\\realinput\\"
identity_name="DRIVINGLICENCE"
id_number="202213456"

        
for filename in os.listdir(imagePath):
    if filename.endswith('.jpg') or filename.endswith('.tif') or filename.endswith('.bmp')or filename.endswith('.png'):
            image = Image.open(os.path.join(imagePath, filename))
            image = image.convert('RGB')
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            image.save(os.path.join(realinput, new_filename))
            print("move to realinput")
            os.remove(os.path.join(imagePath,filename))
            print(filename)
for filename in os.listdir(realinput):
    if filename.endswith('.jpg') or filename.endswith('.tiff') or filename.endswith('.bmp') or filename.endswith('.png'):
# Read the image file
        image_path=os.path.join("F:\\my code\\reverification\\realinput",filename)
        result = func(image_path, id_number,identity_name)
        # result = str(results)
        print("________________KYC CHECKING_____________")
        if filename is None:
            ovd_up = 'no'
        else:
            ovd_up = 'yes'
        # if result != None and isinstance(result[0], str) and len(result) > 0:
        if result != None and len(result) > 0:
        # if result != None:
        # if result != None and isinstance(result[0], str):
            if identity_name == result[1]:  # uploaded and chosen kyc are different
                fake = 'kyc matched'
                print("kyc matched")
                status = 0
                type_kyc = identity_name
            else:
                fake = 'kyc not matched'
                print("kyc not matched")
                status = 1
                type_kyc = result[1]
            if result[1] == 'UIDAICARD(AADHAR)':
                if isinstance(result[0],bool):
                    mask_status = 'Not identified/not clear/vid present'
                else:
                    if id_number[8:] == result[0] and len(result[0]) <= 4:
                        mask_status = 'masked'
                    elif id_number[8:] == result[0][10:] and 4 < len(result[0]) <= 14:
                        mask_status = 'unmasked'
                    else:
                        mask_status = 'Not identified/not clear/vid present'
            else:
                if id_number == result[0] or result[0] == True:
                    mask_status = 'nil'
                else:
                    mask_status = 'nil'
        else:
            print('else-----------')
            mask_status = 'not clear'
            print("not clear")
            status = 2
            type_kyc = 'not clear/other document'
    else:
        print("invalid extension")
    print("-----------------------------------------checking completed---------------------------------------")
    print(result)

