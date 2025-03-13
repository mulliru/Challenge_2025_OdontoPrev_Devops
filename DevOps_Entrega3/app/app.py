import pyodbc
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração do banco de dados
DB_CONFIG = {
    "server": "sql-devops-challenge-553315.database.windows.net",
    "database": "db-devops-challenge",
    "username": "admin_devops",
    "password": "RM_553315@Azure2024!",
    "driver": "ODBC Driver 18 for SQL Server"
}

# Função para conectar ao banco
def connect_db():
    conn_str = (
        f"DRIVER={DB_CONFIG['driver']};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']};"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

# 📌 Endpoint de Teste
@app.route('/')
def home():
    return "🚀 API Flask está rodando!"

# 📌 CRUD - Clientes
@app.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    cpf = data.get("cpf")
    telefone = data.get("telefone")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, cpf, telefone) VALUES (?, ?, ?, ?)", 
                       (nome, email, cpf, telefone))
        conn.commit()
        conn.close()
        return jsonify({"message": "Cliente criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email, cpf, telefone FROM clientes")
        clientes = [{"id": row[0], "nome": row[1], "email": row[2], "cpf": row[3], "telefone": row[4]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(clientes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📌 CRUD - Profissionais
@app.route('/profissionais', methods=['POST'])
def criar_profissional():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    cpf = data.get("cpf")
    cro = data.get("cro")
    especialidade = data.get("especialidade")
    telefone = data.get("telefone")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO profissionais (nome, email, cpf, cro, especialidade, telefone) VALUES (?, ?, ?, ?, ?, ?)", 
                       (nome, email, cpf, cro, especialidade, telefone))
        conn.commit()
        conn.close()
        return jsonify({"message": "Profissional criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/profissionais', methods=['GET'])
def listar_profissionais():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email, cpf, cro, especialidade, telefone FROM profissionais")
        profissionais = [{"id": row[0], "nome": row[1], "email": row[2], "cpf": row[3], "cro": row[4], "especialidade": row[5], "telefone": row[6]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(profissionais)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📌 CRUD - Atendimentos
@app.route('/atendimentos', methods=['POST'])
def criar_atendimento():
    data = request.get_json()
    cliente_id = data.get("cliente_id")
    profissional_id = data.get("profissional_id")
    descricao = data.get("descricao")
    status = data.get("status", "Pendente")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO atendimentos (cliente_id, profissional_id, descricao, status) VALUES (?, ?, ?, ?)", 
                       (cliente_id, profissional_id, descricao, status))
        conn.commit()
        conn.close()
        return jsonify({"message": "Atendimento registrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/atendimentos', methods=['GET'])
def listar_atendimentos():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, cliente_id, profissional_id, data_atendimento, descricao, status FROM atendimentos")
        atendimentos = [{"id": row[0], "cliente_id": row[1], "profissional_id": row[2], "data_atendimento": row[3], "descricao": row[4], "status": row[5]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(atendimentos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📌 CRUD - Pagamentos
@app.route('/pagamentos', methods=['POST'])
def criar_pagamento():
    data = request.get_json()
    atendimento_id = data.get("atendimento_id")
    valor = data.get("valor")
    metodo_pagamento = data.get("metodo_pagamento")
    status = data.get("status", "Pendente")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pagamentos (atendimento_id, valor, metodo_pagamento, status) VALUES (?, ?, ?, ?)", 
                       (atendimento_id, valor, metodo_pagamento, status))
        conn.commit()
        conn.close()
        return jsonify({"message": "Pagamento registrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pagamentos', methods=['GET'])
def listar_pagamentos():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, atendimento_id, valor, metodo_pagamento, data_pagamento, status FROM pagamentos")
        pagamentos = [{"id": row[0], "atendimento_id": row[1], "valor": row[2], "metodo_pagamento": row[3], "data_pagamento": row[4], "status": row[5]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(pagamentos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/sinistros', methods=['POST'])
def criar_sinistro():
    data = request.get_json()
    atendimento_id = data.get("atendimento_id")
    tipo_sinistro = data.get("tipo_sinistro")
    descricao = data.get("descricao")
    status = data.get("status", "Em análise")  # Valor padrão: "Em análise"

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sinistros (atendimento_id, tipo_sinistro, descricao, status) VALUES (?, ?, ?, ?)", 
                       (atendimento_id, tipo_sinistro, descricao, status))
        conn.commit()
        conn.close()
        return jsonify({"message": "Sinistro registrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/sinistros', methods=['GET'])
def listar_sinistros():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, atendimento_id, tipo_sinistro, descricao, data_registro, status FROM sinistros")
        sinistros = [{"id": row[0], "atendimento_id": row[1], "tipo_sinistro": row[2], "descricao": row[3], "data_registro": row[4], "status": row[5]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(sinistros)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    print("🚀 API rodando em: http://127.0.0.1:5000/")
    app.run(host="0.0.0.0", port=5000, debug=True)
