# 📋 Gerenciador de Tarefas com Python e SQLite

Um sistema simples de gerenciamento de tarefas desenvolvido em **Python** utilizando **SQLite** para persistência dos dados. O projeto implementa um CRUD completo (Create, Read, Update, Delete) através de uma interface de linha de comando (CLI).

## 🚀 Funcionalidades

* ✅ Criar tarefas
* 📋 Listar todas as tarefas
* 🔍 Buscar uma tarefa pelo ID
* ✏️ Atualizar título, descrição ou status de uma tarefa
* 🗑️ Excluir tarefas
* 📌 Filtrar tarefas por status
* 💾 Persistência dos dados com SQLite

## 🛠️ Tecnologias utilizadas

* Python 3
* SQLite3
* Pathlib
* Datetime

## 📂 Estrutura do banco de dados

Tabela `tarefas`

| Campo         | Tipo    | Descrição                    |
| ------------- | ------- | ---------------------------- |
| id            | INTEGER | Identificador da tarefa      |
| titulo        | TEXT    | Título da tarefa             |
| descricao     | TEXT    | Descrição da tarefa          |
| status        | TEXT    | aberta, fazendo ou concluida |
| criado_em     | TEXT    | Data de criação              |
| atualizado_em | TEXT    | Data da última atualização   |

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

### 2. Entre na pasta do projeto

```bash
cd nome-do-repositorio
```

### 3. Execute o programa

```bash
python main.py
```

Na primeira execução será criado automaticamente o arquivo:

```text
tarefas.sqlite
```

## 📌 Menu principal

```text
=== Tarefas (SQLite) ===

1. Criar tarefa
2. Listar tarefas
3. Ver tarefa por ID
4. Atualizar tarefa
5. Excluir tarefa
0. Sair
```

## 📝 Exemplos de uso

### Criando uma tarefa

```text
Título: Estudar SQLite
Descrição: Aprender CRUD em Python
Status [aberta/fazendo/concluida]: aberta

Tarefa criada com ID 1.
```

### Listando tarefas

```text
[1] Estudar SQLite | aberta (criado: 2026-06-21T15:30:10)
```

### Atualizando uma tarefa

```text
ID: 1
Novo título: Estudar SQLite e Python
Novo status: fazendo

Atualizada.
```

### Excluindo uma tarefa

```text
ID: 1

Excluída.
```

## 📚 Conceitos praticados

* Funções em Python
* Manipulação de banco de dados SQLite
* SQL (CREATE, INSERT, SELECT, UPDATE e DELETE)
* Context Manager (`with`)
* Tratamento de exceções
* Validação de dados
* List Comprehension
* Manipulação de datas com `datetime`
* Organização e separação de responsabilidades

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com fins de estudo para praticar a integração entre Python e SQLite, além da implementação de operações CRUD e boas práticas de organização de código.

## 👨‍💻 Autor

Lucas Gabriel Nascimento

