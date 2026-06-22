import sqlite3
from pathlib import Path

DB_PATH = Path("tarefas.sqlite")

def exluir_tarefa(tarefa_id):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    con.commit()
    removidas = cur.rowcount
    con.close()
    return removidas > 0

if __name__ == "__main__":
    ok = exluir_tarefa(1)
    print("Excluída." if ok else "Não encontrada.")