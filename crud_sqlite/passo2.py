import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("tarefas.sqlite")

con = sqlite3.connect(DB_PATH)
cur = con.cursor()

# Usamos placeholders (?) para evitar SQL Injection e converter tipos
sql = "INSERT INTO tarefas (titulo, descricao, status, criado_em) VALUES (?, ?, ?, ?)"
dados = (
    "Estudar Python",
    "Ler sobre CRUD e SQLite",
    "aberta",
    datetime.now().isoformat(timespec="seconds") #Formato padrão internacional de data e hora
)

cur.execute(sql, dados)
con.commit()

print("Inserido! ID gerado:", cur.lastrowid) # Pega o ID gerado automaticamente

con.close()