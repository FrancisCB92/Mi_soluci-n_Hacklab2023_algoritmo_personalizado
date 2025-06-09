import random, time

#algoritmo usado
def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + alphabet[(alphabet.index(character) + key) % len(alphabet)]
        for j in range(0, key):
            ciphertext = ciphertext + random.choice(alphabet)
    return ciphertext

#algoritmo para encontrar mensaje oculto
def d_encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + alphabet[(alphabet.index(character) - key) % len(alphabet)]
    ciphertext = ciphertext[::key+1] 
    return ciphertext 

objetivo = "MbzKNclubnQRtOrgmQPnDwtspUfSNCFeqEMiyiVtFmIfGRbsGUzUimiaGvnzpBLfrvzWZimhylZZesgDaH QteTgbQokOheEoorrpaDoZgLhzmN  bfwsFtokyCELaBogwfLAcXoNQKrhCVQJeMVqVMvPvjXEaRXHb QUNLzsvNZRUkGxoibzsTbVucNWdqsypsgjsg sUQykViZUrNuSAXRlZcvZoaxhnRhwJRuAcnHWpRTkkoletByjABhxowKdPVICknvFmDqKc yKhehypGnSniuttNWoWCpNEJxPNixzbDuDucRhsGtkWkdeaxYNDrRoubtRxeJAWFrpcQcIpYFQqWdkwpdEgVKANmIUObWyuAE davlhvBARQyiOptGCEJwVmfeaaJlCHTPazUylFS"

for v in range(0, 50):
    texto = d_encrypt(objetivo, v)
    if " de " in texto or " que " in texto or " a " in texto or " es " in texto:
        print("¡Clave encontrada!: #", v , "// El mensaje secreto es:",  texto)
        break


