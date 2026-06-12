import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path('dados/db-aula.db')
CAMINHO_BANCO.parent.mkdir(exist_ok=True)

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    return conexao

conexao = conectar()

