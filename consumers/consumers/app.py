from chalice import Chalice

app = Chalice(app_name='consumers')

users = {
    "users": [
        {"name": "John Doe", "phone": "123-456-7890"},
        {"name": "Jane Smith", "phone": "987-654-3210"},
        {"name": "Alice Johnson", "phone": "555-123-4567"},
        {"name": "Bob Brown", "phone": "555-987-6543"},
    ]
}
#Essa estrutura de dados é apenas um exemplo e pode ser substituída por uma fonte de dados real, como um banco de dados ou uma API externa.
companies = {
    "companies": [
        {"name": "Acme Corporation", "address": "123 Main St"},
        {"name": "Globex Inc.", "address": "456 Elm St"},
        {"name": "Initech", "address": "789 Oak St"},
        {"name": "Umbrella Corp.", "address": "321 Pine St"},
    ]
}


# CRIAR USUÁRIO
@app.route('/consumers/person', methods=['POST'])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response


# ALTERAR USUÁRIO
@app.route('/consumers/person', methods=['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} atualizado com sucesso!"
    }
    return response


# EXCLUIR USUÁRIO
@app.route('/consumers/person', methods=['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} excluído com sucesso!"
    }
    return response


# CONSULTAR USUÁRIO
@app.route('/consumers/person', methods=['GET'])
def get_persons():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response

@app.route('/consumers/person/{id}', methods=['GET'])
def get_persons(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "John Doe", "phone": "123-456-7890"}}
    }
    return response





# CONSULTAR EMPRESAS
@app.route('/consumers/company', methods=['POST'])
def create_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criada com sucesso!"
    }
    return response           

@app.route('/consumers/company', methods=['PUT'])
def update_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} atualizada com sucesso!"
    }
    return response  


@app.route('/consumers/company', methods=['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} excluída com sucesso!"
    }
    return response  


@app.route('/consumers/companies', methods=['GET'])
def get_companies():
    response = {
        "statusCode": 200,
        "body": companies
    }
    return response  


@app.route('/consumers/companies/{id}', methods=['GET'])
def get_company(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "Acme Corporation", "address": "123 Main St"}}
    }
    return response  

