from fastapi import FastAPI, HTTPException
app= FastAPI()

personagens = {
    1: {
        "nome": "D3rlord3",
        "idade": None,
        "titulo": "receptaculo do rei de amarelo",
        "primeira_aparicao": "footage1.mov",
        "historia": "muito grande",
        "status": "morto",
        "aliados": ["AveryTheMayo"],
        "inimigos": ["Hastur"]
    },

    2: {
        "nome": "AveryTheMayo",
        "idade": 17,
        "titulo": "nenhum kk",
        "primeira_aparicao": "weird book i did NOT write",
        "historia": "muito grande",
        "status": "vivo",
        "aliados": ["D3rlord3"],
        "inimigos": ["Hastur"]
    },

    3: {
        "nome": "Hastur",
        "idade": None,
        "titulo": "O rei de amarelo",
        "primeira_aparicao": "footage2.mov",
        "historia": "muito grande",
        "status": "morto",
        "aliados": None,
        "inimigos": None
    }
}

@app.get("/personagens")
async def get_personagens():
    return personagens

@app.get("/personagens/vivos")
async def get_personagens_vivos():
    vivos = []

    for personagem in personagens:
        if personagens[personagem]["status"] == "vivo":
            vivos.append(personagens[personagem])

    return vivos

@app.get("/personagens/mortos")
async def get_personagens_mortos():
    mortos = []

    for personagem in personagens:
        if personagens[personagem]["status"] == "morto":
            mortos.append(personagens[personagem])

    return mortos

@app.get("/personagens/{id}")
async def get_personagens(id: int):
    if id in personagens:
        return personagens[id]
    else:
        raise HTTPException(status_code=404, detail= "personagem nao encontrado")