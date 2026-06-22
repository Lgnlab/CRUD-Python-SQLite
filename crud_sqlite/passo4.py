import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("tarefas.sqlite")

def atualizar_tarefa(tarefa_id, titulo=None, descricao=None, status=None):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    campos = []
    valores = []

    if titulo is not None:
        campos.append("titulo = ?")
        valores.append(titulo.strip())
    if descricao is not None:
        campos.append("descricao = ?")
        valores.append(descricao.strip())
    if status is not None:
        campos.append("status = ?")
        valores.append(status)

    if not campos:
        print("Nada para atualizar.")
        con.close()
        return False
    
    campos.append("atualizado_em = ?")
    valores.append(datetime.now().isoformat(timespec="seconds"))

    valores.append(tarefa_id)

    sql = f"UPDATE tarefas SET {', '.join(campos)} WHERE id = ?"
    cur.execute(sql, valores)
    con.commit()

    alteradas = cur.rowcount
    con.close()
    return alteradas > 0

if __name__ == "__main__":
    ok = atualizar_tarefa(
        tarefa_id=1,
        status="concluida",
        descricao="Terminei o estudo de CRUD!"
    )
    print("Atualizada." if ok else "Nada foi alterado (ID existe?).")