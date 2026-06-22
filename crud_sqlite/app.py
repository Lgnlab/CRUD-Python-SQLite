import sqlite3
from pathlib import Path
from datetime import datetime
 
DB_PATH = Path("tarefas.sqlite")
 
SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT NOT NULL DEFAULT 'aberta' CHECK (status IN ('aberta','fazendo','concluida')),
    criado_em TEXT NOT NULL,
    atualizado_em TEXT
);
"""
 
def obter_conexao():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con
 
def inicializar_banco():
    with obter_conexao() as con:
        con.execute(SQL_CRIAR_TABELA)
        con.commit()
 
# ---------------- CRUD ----------------
def criar_tarefa(titulo, descricao="", status="aberta"):
    titulo = (titulo or "").strip()
    if not titulo:
        raise ValueError("Título é obrigatório.")
    if status not in ("aberta", "fazendo", "concluida"):
        raise ValueError("Status inválido.")
    agora = datetime.now().isoformat(timespec="seconds")
    with obter_conexao() as con:
        cur = con.execute(
            "INSERT INTO tarefas (titulo, descricao, status, criado_em) VALUES (?, ?, ?, ?)",
            (titulo, (descricao or "").strip(), status, agora),
        )
        con.commit()
        return cur.lastrowid
 
def listar_tarefas(status=None):
    with obter_conexao() as con:
        if status:
            cur = con.execute(
                "SELECT * FROM tarefas WHERE status = ? ORDER BY id", (status,))
        else:
            cur = con.execute("SELECT * FROM tarefas ORDER BY id")
        return [dict(l) for l in cur.fetchall()]
 
def obter_tarefa_por_id(tarefa_id: int):
    with obter_conexao() as con:
        cur = con.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
        row = cur.fetchone()
        return dict(row) if row else None
 
def atualizar_tarefa(tarefa_id: int, *, titulo=None, descricao=None, status=None):
    campos, valores = [], []
    if titulo is not None:
        t = titulo.strip()
        if not t:
            raise ValueError("Título não pode ser vazio.")
        campos.append("titulo = ?")
        valores.append(t)
    if descricao is not None:
        campos.append("descricao = ?")
        valores.append(descricao.strip())
    if status is not None:
        if status not in ("aberta", "fazendo", "concluida"):
            raise ValueError("Status inválido.")
        campos.append("status = ?")
        valores.append(status)
 
    if not campos:
        return False
 
    campos.append("atualizado_em = ?")
    valores.append(datetime.now().isoformat(timespec="seconds"))
    valores.append(tarefa_id)
 
    sql = f"UPDATE tarefas SET {', '.join(campos)} WHERE id = ?"
 
    with obter_conexao() as con:
        cur = con.execute(sql, valores)
        con.commit()
        return cur.rowcount > 0
 
def excluir_tarefa(tarefa_id: int):
    with obter_conexao() as con:
        cur = con.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        con.commit()
        return cur.rowcount > 0
 
# ---------------- CLI ----------------
def mostrar_tarefa(t):
    print("— Detalhes da tarefa —")
    for k in ("id", "titulo", "descricao", "status", "criado_em", "atualizado_em"):
        print(f"{k}: {t.get(k)}")
 
def menu():
    print("\n=== Tarefas (SQLite) ===")
    print("1. Criar tarefa")
    print("2. Listar tarefas (opcional: filtrar por status)")
    print("3. Ver tarefa por ID")
    print("4. Atualizar tarefa")
    print("5. Excluir tarefa")
    print("0. Sair")
    return input("Escolha: ").strip()
 
def main():
    inicializar_banco()
    while True:
        opc = menu()
        try:
            if opc == "1":
                titulo = input("Título: ")
                descricao = input("Descrição (opcional): ")
                status = input("Status [aberta/fazendo/concluida] (Enter=aberta): ").strip() or "aberta"
                novo_id = criar_tarefa(titulo, descricao, status)
                print(f"Tarefa criada com ID {novo_id}.")
            elif opc == "2":
                filtro = input("Filtrar por status (Enter = todos): ").strip() or None
                tarefas = listar_tarefas(filtro)
                if not tarefas:
                    print("Sem tarefas.")
                else:
                    for t in tarefas:
                        print(f"[{t['id']}] {t['titulo']} | {t['status']} (criado: {t['criado_em']})")
            elif opc == "3":
                tid = int(input("ID: "))
                t = obter_tarefa_por_id(tid)
                if t:
                    mostrar_tarefa(t)
                else:
                    print("Não encontrada.")
            elif opc == "4":
                tid = int(input("ID: "))
                novo_titulo = input("Novo título (Enter = manter): ").strip()
                nova_desc = input("Nova descrição (Enter = manter): ").strip()
                novo_status = input("Novo status [aberta/fazendo/concluida] (Enter = manter): ").strip()
                ok = atualizar_tarefa(
                    tid,
                    titulo=novo_titulo or None,
                    descricao=nova_desc or None,
                    status=novo_status or None,
                )
                print("Atualizada." if ok else "Nada alterado (ID existe?).")
            elif opc == "5":
                tid = int(input("ID: "))
                ok = excluir_tarefa(tid)
                print("Excluída." if ok else "Não encontrada.")
            elif opc == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")
        except ValueError as e:
            print("Entrada inválida:", e)
        except sqlite3.IntegrityError as e:
            print("Regra do banco violada:", e)
 
if __name__ == "__main__":
    main()