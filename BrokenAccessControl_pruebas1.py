import secrets

def generar_php_sessid():
    return secrets.token_hex(16)  # 16 bytes = 32 caracteres hexadecimales

# sessid = generar_php_sessid()
# print(f"PHPSESSID simulado: {sessid}")

for n in range(30):
    sessid = generar_php_sessid()
    print(sessid)
