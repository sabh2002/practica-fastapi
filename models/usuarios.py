from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

usuarios = Table('Usuarios', meta, Column(
        'id', Integer, primary_key=True),
         Column('nombre', String(255)),
         Column('correo', String(255)),
         Column('clave', String(255)))
meta.create_all(engine)