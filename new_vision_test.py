import os,time
from google.cloud import vision
import re
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision-377709-7ecf57251a35.json'
client = vision.ImageAnnotatorClient()
def func(path,kyc_no,identity_name):
    print("inside kyc the function")
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if len(texts) > 0:
        # Get the first block of text (assumed to be the title)
        title = texts[0].description
        # print(title)
        new=title.split()
        # print(new)
        new=[i.lower() for i in new]
        print(new)
        print('________________________________________________')
        # Extract Aadhar and PAN card numbers from the title using regular expressions
        aadhar_pattern = '[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}'
        aadhar_number = re.search(aadhar_pattern, title)
        pan_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]{1}'
        voters_id_pattern = r'[A-Z]{3}[0-9]{7}'
        passport_pattern = r'[A-Z]{1}[0-9]{7}'
        if identity_name=='DRIVINGLICENCE':
            if "motor" in new or "driving" in new or "licence" in new or "lmv" in new or "mcwg" in new or "licencing" in new or "dl" in new or "transport" in new or "non-transport" in new or kyc_no in new:
                dl_pattern = r'[A-Z]{2}\d{2}(?:\d{2})?\d{7}'
                dl_number = re.search(dl_pattern, title)
                if dl_number:
                    dl_no = dl_number.group(0)
                    os.remove(path)
                    print("File removed successfully")
                    print('Driving license identified')
                    return (dl_no, 'DRIVINGLICENCE')
                else:
                    os.remove(path)
                    print("File removed successfully")
                    return (True, 'DRIVINGLICENCE')
            elif aadhar_number:
                aadhar_no=aadhar_number.group(0)
                os.remove(path)
                print("file removed successfully")
                print('aadhar unmasked')
                return (aadhar_no,'UIDAICARD(AADHAR)')
            elif "year of birth" in new or "vid" in new or "unique" in new or "identification" in new or "aadhar" in new or "aadhaar" in new or "authenticate" in new or "enrollment" in new or kyc_no[8:] in new:
                if kyc_no[8:] in new:
                    os.remove(path)
                    print("file removed successfully")
                    print('aadhar masked')
                    return(kyc_no[8:],'UIDAICARD(AADHAR)')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return(True,'UIDAICARD(AADHAR)')
            elif "election" in new or "commission"in new or 'elector' in new or 'electoral' in new or kyc_no in new:
                voterid_number = re.search(voters_id_pattern, title)
                if voterid_number:
                    voter_id_num=voterid_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    return (voter_id_num,'COPYOFVOTERSID')
                    # return (True,'COPY OF VOTERSID')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    # return (kyc_no,'COPY OF VOTERSID')
                    return (True,'COPYOFVOTERSID')
            elif 'republic' in new or "country" in new or 'nationality' in new or "type" in new or kyc_no in new:
                passport_number = re.search(passport_pattern, title)
                if passport_number:
                    passport_no=passport_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    return (passport_no,'PASSPORT')
                    # return (True,'PASSPORT')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    # return (kyc_no,'PASSPORT')
                    return (True,'PASSPORT')
            elif "income" in new or "tax" in new or "department" in new or "permanent" in new or "govt of india" in new or "account" in new:
                pan_number = re.search(pan_pattern, title)
                if pan_number:
                    pancard_no=pan_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    return (pancard_no,'PANCARD')
                    # return (True,'PANCARD')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return (True,'PANCARD')
        elif identity_name=='UIDAICARD(AADHAR)':
            if aadhar_number:
                aadhar_no=aadhar_number.group(0)
                os.remove(path)
                print("file removed successfully")
                print('aadhar unmasked')
                return (aadhar_no,'UIDAICARD(AADHAR)')
            elif "year of birth" in new or "vid" in new or "unique" in new or "identification" in new or "aadhar" in new or "aadhaar" in new or "authenticate" in new or "enrollment" in new or kyc_no[8:] in new:
                if kyc_no[8:] in new:
                    os.remove(path)
                    print("file removed successfully")
                    print('aadhar masked')
                    return(kyc_no[8:],'UIDAICARD(AADHAR)')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return(True,'UIDAICARD(AADHAR)')
            elif "motor" in new or "driving" in new or "licence" in new or "lmv" in new or "mcwg" in new or "licencing" in new or "dl" in new or "transport" in new or "non-transport" in new or kyc_no in new:
                dl_pattern = r'[A-Z]{2}\d{2}(?:\d{2})?\d{7}'
                dl_number = re.search(dl_pattern, title)
                if dl_number:
                    dl_no = dl_number.group(0)
                    os.remove(path)
                    print("File removed successfully")
                    print('Driving license identified')
                    return (dl_no, 'DRIVINGLICENCE')
                else:
                    os.remove(path)
                    print("File removed successfully")
                    return (True, 'DRIVINGLICENCE')
            elif "election" in new or "commission"in new or 'elector' in new or 'electoral' in new or kyc_no in new:
                voterid_number = re.search(voters_id_pattern, title)
                if voterid_number:
                    voter_id_num=voterid_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    return (voter_id_num,'COPYOFVOTERSID')
                    # return (True,'COPY OF VOTERSID')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    # return (kyc_no,'COPY OF VOTERSID')
                    return (True,'COPYOFVOTERSID')
            elif 'republic' in new or "country" in new or 'nationality' in new  or "type" in new or kyc_no in new:
                passport_number = re.search(passport_pattern, title)
                if passport_number:
                    passport_no=passport_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    return (passport_no,'PASSPORT')
                    # return (True,'PASSPORT')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    # return (kyc_no,'PASSPORT')
                    return (True,'PASSPORT')
            elif "income" in new or "tax" in new or "department" in new or "permanent" in new or "govt of india" in new or "account" in new:
                pan_number = re.search(pan_pattern, title)
                if pan_number:
                    pancard_no=pan_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    return (pancard_no,'PANCARD')
                    # return (True,'PANCARD')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return (True,'PANCARD')
        elif identity_name=='COPYOFVOTERSID':
            if "election" in new or "commission"in new or 'elector' in new or 'electoral' in new or kyc_no in new:
                voterid_number = re.search(voters_id_pattern, title)
                if voterid_number:
                    voter_id_num=voterid_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    return (voter_id_num,'COPYOFVOTERSID')
                    # return (True,'COPY OF VOTERSID')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    # return (kyc_no,'COPY OF VOTERSID')
                    return (True,'COPYOFVOTERSID')
            elif "motor" in new or "driving" in new or "licence" in new or "lmv" in new or "mcwg" in new or "licencing" in new or "dl" in new or "transport" in new or "non-transport" in new or kyc_no in new:
                dl_pattern = r'[A-Z]{2}\d{2}(?:\d{2})?\d{7}'
                dl_number = re.search(dl_pattern, title)
                if dl_number:
                    dl_no = dl_number.group(0)
                    os.remove(path)
                    print("File removed successfully")
                    print('Driving license identified')
                    return (dl_no, 'DRIVINGLICENCE')
                else:
                    os.remove(path)
                    print("File removed successfully")
                    return (True, 'DRIVINGLICENCE')
            elif aadhar_number:
                aadhar_no=aadhar_number.group(0)
                os.remove(path)
                print("file removed successfully")
                print('aadhar unmasked')
                return (aadhar_no,'UIDAICARD(AADHAR)')
            elif "year of birth" in new or "vid" in new or "unique" in new or "identification" in new or "aadhar" in new or "aadhaar" in new or "authenticate" in new or "enrollment" in new or kyc_no[8:] in new:
                if kyc_no[8:] in new:
                    os.remove(path)
                    print("file removed successfully")
                    print('aadhar masked')
                    return(kyc_no[8:],'UIDAICARD(AADHAR)')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return(True,'UIDAICARD(AADHAR)')
            elif 'republic' in new or "country" in new or 'nationality' in new or "type" in new or kyc_no in new:
                passport_number = re.search(passport_pattern, title)
                if passport_number:
                    passport_no=passport_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    return (passport_no,'PASSPORT')
                    # return (True,'PASSPORT')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    # return (kyc_no,'PASSPORT')
                    return (True,'PASSPORT')
            elif "income" in new or "tax" in new or "department" in new or "permanent" in new or "govt of india" in new or "account" in new:
                pan_number = re.search(pan_pattern, title)
                if pan_number:
                    pancard_no=pan_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    return (pancard_no,'PANCARD')
                    # return (True,'PANCARD')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return (True,'PANCARD')
        elif identity_name=='PASSPORT':
            if 'republic' in new or "country" in new or 'nationality' in new or "type" in new or kyc_no in new:
                passport_number = re.search(passport_pattern, title)
                if passport_number:
                    passport_no=passport_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    return (passport_no,'PASSPORT')
                    # return (True,'PASSPORT')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    # return (kyc_no,'PASSPORT')
                    return (True,'PASSPORT')
            elif "election" in new or "commission"in new or 'elector' in new or 'electoral' in new or kyc_no in new:
                voterid_number = re.search(voters_id_pattern, title)
                if voterid_number:
                    voter_id_num=voterid_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    return (voter_id_num,'COPYOFVOTERSID')
                    # return (True,'COPY OF VOTERSID')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    # return (kyc_no,'COPY OF VOTERSID')
                    return (True,'COPYOFVOTERSID')
            elif "motor" in new or "driving" in new or "licence" in new or "lmv" in new or "mcwg" in new or "licencing" in new or "dl" in new or "transport" in new or "non-transport" in new or kyc_no in new:
                dl_pattern = r'[A-Z]{2}\d{2}(?:\d{2})?\d{7}'
                dl_number = re.search(dl_pattern, title)
                if dl_number:
                    dl_no = dl_number.group(0)
                    os.remove(path)
                    print("File removed successfully")
                    print('Driving license identified')
                    return (dl_no, 'DRIVINGLICENCE')
                else:
                    os.remove(path)
                    print("File removed successfully")
                    return (True, 'DRIVINGLICENCE')
            elif aadhar_number:
                aadhar_no=aadhar_number.group(0)
                os.remove(path)
                print("file removed successfully")
                print('aadhar unmasked')
                return (aadhar_no,'UIDAICARD(AADHAR)')
            elif "year of birth" in new or "vid" in new or "unique" in new or "identification" in new or "aadhar" in new or "aadhaar" in new or "authenticate" in new or "enrollment" in new or kyc_no[8:] in new:
                if kyc_no[8:] in new:
                    os.remove(path)
                    print("file removed successfully")
                    print('aadhar masked')
                    return(kyc_no[8:],'UIDAICARD(AADHAR)')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return(True,'UIDAICARD(AADHAR)')
            elif "income" in new or "tax" in new or "department" in new or "permanent" in new or "govt of india" in new or "account" in new:
                pan_number = re.search(pan_pattern, title)
                if pan_number:
                    pancard_no=pan_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    return (pancard_no,'PANCARD')
                    # return (True,'PANCARD')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return (True,'PANCARD')
        if identity_name=='PANCARD':
            if "income" in new or "tax" in new or "department" in new or "permanent" in new or "govt of india" in new or "account" in new:
                pan_number = re.search(pan_pattern, title)
                if pan_number:
                    pancard_no=pan_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    return (pancard_no,'PANCARD')
                    # return (True,'PANCARD')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return (True,'PANCARD')
            if 'republic' in new or "country" in new or 'nationality' in new or "type" in new or kyc_no in new:
                passport_number = re.search(passport_pattern, title)
                if passport_number:
                    passport_no=passport_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    return (passport_no,'PASSPORT')
                    # return (True,'PASSPORT')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('passport identified')
                    # return (kyc_no,'PASSPORT')
                    return (True,'PASSPORT')
            elif "election" in new or "commission"in new or 'elector' in new or 'electoral' in new or kyc_no in new:
                voterid_number = re.search(voters_id_pattern, title)
                if voterid_number:
                    voter_id_num=voterid_number.group(0)
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    return (voter_id_num,'COPYOFVOTERSID')
                    # return (True,'COPY OF VOTERSID')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    print('election id identified')
                    # return (kyc_no,'COPY OF VOTERSID')
                    return (True,'COPYOFVOTERSID')
            elif "motor" in new or "driving" in new or "licence" in new or "lmv" in new or "mcwg" in new or "licencing" in new or "dl" in new or "transport" in new or "non-transport" in new or kyc_no in new:
                dl_pattern = r'[A-Z]{2}\d{2}(?:\d{2})?\d{7}'
                dl_number = re.search(dl_pattern, title)
                if dl_number:
                    dl_no = dl_number.group(0)
                    os.remove(path)
                    print("File removed successfully")
                    print('Driving license identified')
                    return (dl_no, 'DRIVINGLICENCE')
                else:
                    os.remove(path)
                    print("File removed successfully")
                    return (True, 'DRIVINGLICENCE')
            elif aadhar_number:
                aadhar_no=aadhar_number.group(0)
                os.remove(path)
                print("file removed successfully")
                print('aadhar unmasked')
                return (aadhar_no,'UIDAICARD(AADHAR)')
            elif "year of birth" in new or "vid" in new or "unique" in new or "identification" in new or "aadhar" in new or "aadhaar" in new or "authenticate" in new or "enrollment" in new or kyc_no[8:] in new:
                if kyc_no[8:] in new:
                    os.remove(path)
                    print("file removed successfully")
                    print('aadhar masked')
                    return(kyc_no[8:],'UIDAICARD(AADHAR)')
                else:
                    os.remove(path)
                    print("file removed successfully")
                    return(True,'UIDAICARD(AADHAR)')
            

        else:
            os.remove(path)
            print("file removed successfully")
            return None