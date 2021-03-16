import os
import hashlib
import random
import string
def ranstr(num):
    # ramdom
    idonotknow = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(idonotknow)

    return salt

print('\n1.Use the master password to generate your password 2.A random password')
flag = int(input('your choice：'))
if flag == 1:
    firsttext = input('\nyour master passwd：')
    secondtext = input('\nThe domain name of the website using the password：')
    maintext =  firsttext + secondtext
    print ("now text is : ", maintext)
    text1 = hashlib.sha512()
    text1.update(maintext.encode('utf-8'))
    res = text1.hexdigest()
    textfinal = hashlib.sha512()
    textfinal.update(res.encode('utf-8'))
    finalres = textfinal.hexdigest()
    code1 = finalres[0:7]
    code2 = finalres[-7:]
    code1 = code1.upper()
    thepasswd = code1 + code2
    '''
    print("first:",code1)
    print("second:",code2)
    print("the end:",finalres)
    '''
    print("passwd is:",thepasswd)
elif flag == 2:
    salt = ranstr(28)
    ramtext = hashlib.sha256()
    ramtext.update(salt.encode('utf-8'))
    ramres = ramtext.hexdigest()
    codex = ramres[0:7]
    codez = ramres[-7:]
    codez = codez.upper()
    rampasswd = codex + codez
    print("passwd is:",rampasswd)
