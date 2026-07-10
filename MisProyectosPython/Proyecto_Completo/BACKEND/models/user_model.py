
from db import db

def obtener_todos():
    return db.usuario.find_many(order={"id": "desc"})

def obtener_usuario_por_id(id):
    return db.usuario.find_unique(where={"id": id})