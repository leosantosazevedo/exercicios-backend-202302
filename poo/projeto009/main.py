import fastapi

app = fastapi.FastAPI()
menu = [{'id': 1,        'name': 'coffee',      'price': 2.5     },
        {'id': 2,        'name': 'cake',        'price': 10    },
        {'id': 3,        'name': 'tea',         'price': 3.2    },
        {'id': 4,        'name': 'croissant',   'price': 5.79    }]

@app.get("/")
def hello_world_root():
    return {"Turma": "Backend"}

@app.get("/list-menu")
def list_menu():
    return {"Menu": menu }