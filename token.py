import jwt
import datetime

# Chave secreta usada para assinar os tokens
SECRET_KEY = "sua_chave_secreta_aqui"

# Função para gerar um token JWT
def gerar_token(user_id, secret_key, expiration_minutes):
    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
    payload = {"user_id": user_id, "exp": exp}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

# Função para validar um token JWT
def validar_token(received_token, secret_key):
    try:
        payload = jwt.decode(received_token, secret_key, algorithms=["HS256"])
        user_id = payload["user_id"]
        return True, user_id
    except jwt.ExpiredSignatureError:
        return False, "Token expirado."
    except jwt.InvalidTokenError:
        return False, "Token inválido."

# Configuração inicial
USER_ID = "12345"
EXPIRATION_MINUTES = 30

# Gerar um token
token = gerar_token(USER_ID, SECRET_KEY, EXPIRATION_MINUTES)
print(f"Token gerado: {token}")

# Validar o token
is_valid, result = validar_token(token, SECRET_KEY)
if is_valid:
    print(f"Token válido. User ID: {result}")
else:
    print(f"Token inválido. Motivo: {result}")

# Testar com um token expirado ou modificado
invalid_token = token + "abc"  # Modificando o token para torná-lo inválido
is_valid, result = validar_token(invalid_token, SECRET_KEY)
if is_valid:
    print(f"Token válido. User ID: {result}")
else:
    print(f"Token inválido. Motivo: {result}")
