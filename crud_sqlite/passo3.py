import sqlite3
from pathlib import Path

DB_PATH = Path("tarefas.sqlite")

# row_factory permite ler por nome da coluna
con = sqlite3.connect(DB_PATH)
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("SELECT * FROM tarefas ORDER BY id")
linhas = cur.fetchall() # Busca todas as linhas

if not linhas:
    print("Não há tarefas.")
else:
    for linha in linhas:
        # linha é um "Row", dá pra usar dict(linha)
        t = dict(linha)
        print(f"[{t['id']}] {t['titulo']} | {t['status']} (criado: {t['criado_em']})")

con.close()