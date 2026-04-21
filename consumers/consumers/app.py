# Importa a classe Chalice, que é usada para criar APIs serverless na AWS Lambda
from chalice import Chalice

# Cria a aplicação Chalice e define o nome do app
app = Chalice(app_name='consumers')


# Simulação de um "banco de dados" em memória (lista de usuários)
users = {
    "users": [
        {"name": "John Doe", "phone": "123-456-7890"},
        {"name": "Jane Smith", "phone": "987-654-3210"},
        {"name": "Alice Johnson", "phone": "555-123-4567"},
        {"name": "Bob Brown", "phone": "555-987-6543"},
    ]
}

# Essa estrutura é apenas um exemplo.
# Em produção, o ideal seria usar banco de dados (DynamoDB, RDS, etc.)
companies = {
    "companies": [
        {"name": "Acme Corporation", "address": "123 Main St"},
        {"name": "Globex Inc.", "address": "456 Elm St"},
        {"name": "Initech", "address": "789 Oak St"},
        {"name": "Umbrella Corp.", "address": "321 Pine St"},
    ]
}


# =========================
# ROTAS DE USUÁRIOS (PERSON)
# =========================

# Rota para CRIAR usuário (HTTP POST)
@app.route('/consumers/person', methods=['POST'])
def create_user():
    # Captura o corpo da requisição (JSON enviado pelo cliente)
    requests_params = app.current_request.json_body
    
    # Retorna uma resposta simulando sucesso
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response


# Rota para ATUALIZAR usuário (HTTP PUT)
@app.route('/consumers/person', methods=['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} atualizado com sucesso!"
    }
    return response


# Rota para EXCLUIR usuário (HTTP DELETE)
@app.route('/consumers/person', methods=['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} excluído com sucesso!"
    }
    return response


# Rota para LISTAR todos os usuários (HTTP GET)
@app.route('/consumers/persons', methods=['GET'])
def get_persons():
    response = {
        "statusCode": 200,
        # Retorna todos os usuários do "banco"
        "body": users
    }
    return response


# Rota para BUSCAR um usuário específico pelo ID (path parameter)
@app.route('/consumers/person/{id}', methods=['GET'])
def get_person(id):
    response = {
        "statusCode": 200,
        # Retorno fixo (mock). Em produção, buscaria pelo ID real
        "body": {id: {"name": "John Doe", "phone": "123-456-7890"}}
    }
    return response



# =========================
# ROTAS DE EMPRESAS (COMPANY)
# =========================

# Rota para CRIAR empresa
@app.route('/consumers/company', methods=['POST'])
def create_company():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criada com sucesso!"
    }
    return response           


# Rota para ATUALIZAR empresa
@app.route('/consumers/company', methods=['PUT'])
def update_company():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} atualizada com sucesso!"
    }
    return response  


# Rota para EXCLUIR empresa
@app.route('/consumers/company', methods=['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body
    
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} excluída com sucesso!"
    }
    return response  


# Rota para LISTAR todas as empresas
@app.route('/consumers/companies', methods=['GET'])
def get_companies():
    response = {
        "statusCode": 200,
        # Retorna todas as empresas
        "body": companies
    }
    return response  


# Rota para BUSCAR uma empresa específica pelo ID
@app.route('/consumers/company/{id}', methods=['GET'])
def get_company(id):
    response = {
        "statusCode": 200,
        # Retorno mockado (fixo)
        "body": {id: {"name": "Acme Corporation", "address": "123 Main St"}}
    }
    return response  