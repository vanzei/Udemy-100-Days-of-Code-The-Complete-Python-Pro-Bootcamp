def encrypt(text, shift):
    
    numbers = [ord(char) for char in text.lower()]
    encry = [x+shift for x in numbers]
    text_encode = [chr(x) for x in encry]
    
    return ''.join(text_encode)

def decrypt(text, shift):
    numbers = [ord(char) for char in text.lower()]
    encry = [x-shift for x in numbers]
    text_decoded = [chr(x) for x in encry]
    return ''.join(text_decoded)

a, b = str(input('Enter your text to enconde: \n')), int(input('Enter your shift value (number): \n'))

code = encrypt(a, b)

print(f'Encoded text {code}')

decode = decrypt(code, b)

print(f'Decoded text {decode}')