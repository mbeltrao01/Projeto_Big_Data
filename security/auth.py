import logging
logging.basicConfig(filename='access.log', level=logging.INFO)

def log_user_access(user_id):
    logging.info(f"Usuário {user_id} acessou o sistema.")