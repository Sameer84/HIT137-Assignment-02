def decrypt(cryptogram, shift):
    decrypted_text = ""
    for char in cryptogram:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def find_shift_key(cryptogram):
    for shift in range(1, 26):
        decrypted_text = decrypt(cryptogram, shift)
        print(f"Shift Key: {shift}, Decrypted Text: {decrypted_text}")

# Provided cryptogram
cryptogram = "VZ FRYSVFU VZCNGVIRAG NAQ N YUGGYR VAFRPHEIR V ZNXR ZVEGNXRF V NZ BHG US PRAGEBY NAQNG GVZRE UNEQ GB UNAQYIR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LOH HER N URYYQBAG URFREIR ZR NG ZL ORFG ZNEVYLA ZEAEBR"

# Find the shift key(s)
find_shift_key(cryptogram)