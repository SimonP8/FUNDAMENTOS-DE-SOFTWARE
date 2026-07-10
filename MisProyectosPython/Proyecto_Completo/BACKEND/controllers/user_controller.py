
from models import user_model

def listar_usuarios():
    usuarios = user_model.obtener_todos()
    return [u.dict() for u in usuarios], 200