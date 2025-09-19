# Importar librerías
from fastapi import FastAPI
from pydantic import BaseModel

# Objeto Base Model
class Item(BaseModel):
    name : str
    description: str | None = None
    price : float
    tax : float

# Creamos la aplicación FastAPI.
# Esto inicializa la API y nos permitirá definir endpoints.
app = FastAPI()

# Añadirle un endpoint a la app: El decorador @app.get("/") indica que se responderán solicitudes GET en esta ruta.
# @ : Añadirle una funcionalidad extra a la función que yo quiero

# Cuando accedamos a este endpoint, nos regresara el string "Hello World"
@app.get("/") # Path raíz

# El async es para poder ejecutar varias funciones a la vez si es que no dependen una de la otra
async def hello_world(): # El nombre de la función no influye tanto
    return 'Hello World'

@app.get("/api/v1/items/{item_id}")
async def read_items(item_id:int):
    return {"item_id":item_id}

# Ahora un método post
# Este no funciona en terminal solo en postman
# Usamos la clase Item para verificar el tipo del dato [no lo cambia, solo te arroja error de type]
@app.post("/api/v1/items/")
async def create_item(item : Item):
    return (f'El item {item.name} es: {item.description}, cuesta {item.price} y tiene un impuesto de {item.tax}')



