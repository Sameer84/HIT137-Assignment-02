#This is encrypt function which takes a plaintext and a key
def encrypt(text, key):
    encrypted_text = ""
    for char in text: #Iterates over each character
        if char.isalpha():#If character is alphabetic
            shifted = ord(char) + key#calculates the shifted value by adding the key to the ASCII value of the character
            if char.islower():#if character is lowercase
                #if the character is beyond the lowercase range('a' to 'z')
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            #If the character is uppercase
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            # non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text
#Function to decrypt an encrypted text    
def decrypt(encrypted_code, key):
    return encrypt(encrypted_code, -key)
#key value result from find_key.py program
key = 13
#Encrypted code
encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr 
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]
    
    juvyr ybpny_inevnoyr > 0: 
        vs ybpny_inevnoyr % 2 == 0: 
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1
    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcongr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")
    
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""
# call decrypt function with value of encrypted_code and key
decrypted_code = decrypt(encrypted_code, key)

# Result of decrypted code
print(decrypted_code)
