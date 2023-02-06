from fastapi import APIRouter
from config.db import connection
from models.usuarios import usuarios
from schemas.schemas import Usuario
from cryptography.fernet import Fernet

key = Fernet.generate_key()

encriptar = Fernet(key)

principal = APIRouter()

@principal.get('/usuarios')
async def get_usuarios():
    return connection.execute(usuarios.select()).fetchall()

@principal.post('/usuarios')
async def crear_usuario(usuario: Usuario):
    nuevo_usuario = {'nombre': usuario.nombre,
                    'correo': usuario.correo}
    nuevo_usuario['clave']=encriptar.encrypt(usuario.clave.encode('utf-8'))
    resultado = connection.execute(usuarios.insert().values(nuevo_usuario))
    print(type(resultado))
    return "Hola usuario"
