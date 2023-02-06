from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[str]
    nombre: str
    correo: str
    clave: str