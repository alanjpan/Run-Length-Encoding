code = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def runlength_encrypt(code):
    print('encrypt: ' + code)
    encrypt = ''
    encode = ''
    count = 1
    encode = code[0]
    for i in range(1, len(code)):
        if encode == code[i]:
            count += 1
        else:
            encrypt += str(count)
            encrypt += str(encode)
            encode = code[i]
            count = 1
    encrypt += str(count)
    encrypt += str(encode)
    print('encryption: ' + encrypt)
    return encrypt

def runlength_decrypt(crypt):
    stri = ''
    num = 0
    decrypt = ''
    for i in range(len(crypt)):
        try: 
            if int(crypt[i]):
                stri += crypt[i]
        except:
            num = int(stri)
            stri = ''
            for j in range(num):
                decrypt += crypt[i]
    print('decrypt: ' + decrypt)
    length_crypt = len(crypt)
    length_raw = len(decrypt)
    efficient = round(length_crypt / length_raw, 3)
    print('efficiency: ' + str(efficient))

crypt = runlength_encrypt(code)
runlength_decrypt(crypt)