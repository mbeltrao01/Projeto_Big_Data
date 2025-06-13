import logging
logging.basicConfig(filename='access.log', level=logging.INFO)
from werkzeug.security import check_password_hash, generate_password_hash

# Usuários simulados (em produção, use banco seguro)
USERS = {
    "admin": generate_password_hash("senha123"),
    # Adicione mais usuários conforme necessário
}

# Função de autenticação

def authenticate(username, password):
    if username in USERS and check_password_hash(USERS[username], password):
        return True
    return False

def log_user_access(user_id):
    logging.info(f"Usuário {user_id} acessou o sistema.")

# Estrutura para MFA (exemplo, não implementado)
# def verify_mfa_code(user_id, code):
#     # Aqui você integraria com serviço de MFA externo
#     return True  # Simulação