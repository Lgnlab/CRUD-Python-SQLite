import sqlite3
from pathlib import Path

DB_PATH = Path("tarefas.sqlite") # Caminho e nome do banco de dados

SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT NOT NULL DEFAULT 'aberta',
    criado_em TEXT NOT NULL,
    atualizado_em TEXT
);
"""

# 1) abre (ou cria) o arquivo do banco
con = sqlite3.connect(DB_PATH)

# 2) cria um "cursor" para enviar comandos SQL
cur = con.cursor()

# 3) cria a tabela se não existir
cur.execute(SQL_CRIAR_TABELA)

# 4) salva a alteração (commit) e fecha
con.commit()
con.close()

print("Banco inicializado: tarefas.sqlite e tabela criada (se não existia).")