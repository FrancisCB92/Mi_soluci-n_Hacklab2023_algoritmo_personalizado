alph = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á',
    'é', 'í', 'ó', 'ú', ',', '.', ' '
]

c_msgs = ["wiqxmvb"
, "wiqxmvduyidxydpeqsdiwdpmdgevmgmeb"
,"wiqxmvduyidxydwyirsdiwdpmdhiwisb"
, "wiqxmvduyidxydpmvehediwdpmdhiwgeqwsb"
,"wiqxmvduyidxydqspfvidiwdpmdgeqgm qb"
,"wiqxmvduyidxydfsgediwdpmdvijykmsb"
,"wiqxmvduyidxydeopediwdpmdvikeosc"
,"wiqxmvduyidiémwxiwccc"
,"wiqxmvduyidzmzsdtevedepevxic"
]

j_alph = "".join(alph)
frag_txt = "wiqxmvduyidxyd"

def encrypt(plaintext, key):
    alphabet = j_alph
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + alphabet[(alphabet.index(character) + key) % len(alphabet)]
    return ciphertext

test_1 = encrypt("hola mundo", 3)
print("Test 1:", test_1) 

def d_encrypt(plaintext, key):
    alphabet = j_alph
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + alphabet[(alphabet.index(character) - key) % len(alphabet)]
    return ciphertext 

for msg in c_msgs:
  texto = d_encrypt(msg, 4)
  print(msg, texto)
