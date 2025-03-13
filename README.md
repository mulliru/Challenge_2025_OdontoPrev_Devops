# CHALLENGE_DEVOPS_TOOLS_CLOUD_COMPUTING - API para Gerenciamento Odontológico

## Integrantes:
- **Murilo Ferreira Ramos** - RM553315
- **Pedro Luiz Prado** - RM553874
- **William Kenzo Hayashi** - RM552659

## Distribuição de Atividades
A divisão das atividades foi realizada conforme as disciplinas da grade curricular:

- **Murilo**: DevOps Tools, Cloud Computing, Compliance, Quality Assurance, e Tests.
- **Pedro**: Mobile Application Development, e Advanced Business Development With .NET.
- **William**: Java Advanced, Mastering Relational e Non-Relational Database, Disruptive Architectures IoT, IOB, Generative AI.

## Cronograma de Tarefas
- [Link do Trello](https://trello.com/invite/b/6701a3ed3d57ce4ab46300fd/ATTI2c7cf38c5ce5cc04465175370f7a3aedF74A7B2D/backlog-odontoprev)

## Rodagem da Aplicação
Para executar a API, siga os passos abaixo:

1. **Subir os containers**:
   ```sh
   docker-compose up -d
   ```
2. **Verificar logs da API**:
   ```sh
   docker logs -f api-devops-challenge
   ```
3. **Testar a API**:
   - Para verificar se a API está rodando:
     ```sh
     curl http://localhost:5000
     ```
   - Para visualizar os clientes cadastrados:
     ```sh
     curl -X GET http://localhost:5000/clientes
     ```

## Listagem de Endpoints

### **1. Criar Cliente**
- **Método**: POST
- **URL**: `http://localhost:5000/clientes`
- **Body**:
  ```json
  {
    "nome": "João Silva",
    "email": "joao@example.com",
    "cpf": "123.456.789-00",
    "telefone": "(11) 99999-9999"
  }
  ```
- **Respostas**:
  - `201 Created`: Cliente criado com sucesso.
  - `500 Internal Server Error`: Erro ao cadastrar cliente.

### **2. Obter Todos os Clientes**
- **Método**: GET
- **URL**: `http://localhost:5000/clientes`
- **Respostas**:
  - `200 OK`: Retorna a lista de clientes cadastrados.
  - `500 Internal Server Error`: Erro ao buscar clientes.

### **3. Criar Profissional**
- **Método**: POST
- **URL**: `http://localhost:5000/profissionais`
- **Body**:
  ```json
  {
    "nome": "Dra. Fernanda Souza",
    "email": "fernanda@example.com",
    "cpf": "987.654.321-00",
    "cro": "123456-SP",
    "especialidade": "Ortodontia",
    "telefone": "(11) 99999-7777"
  }
  ```
- **Respostas**:
  - `201 Created`: Profissional cadastrado com sucesso.
  - `500 Internal Server Error`: Erro ao cadastrar profissional.

### **4. Criar Atendimento**
- **Método**: POST
- **URL**: `http://localhost:5000/atendimentos`
- **Body**:
  ```json
  {
    "cliente_id": 1,
    "profissional_id": 1,
    "descricao": "Consulta de avaliação",
    "status": "Pendente"
  }
  ```
- **Respostas**:
  - `201 Created`: Atendimento registrado com sucesso.
  - `500 Internal Server Error`: Erro ao cadastrar atendimento.

### **5. Criar Pagamento**
- **Método**: POST
- **URL**: `http://localhost:5000/pagamentos`
- **Body**:
  ```json
  {
    "atendimento_id": 1,
    "valor": 200.00,
    "metodo_pagamento": "Cartão de Crédito",
    "status": "Pendente"
  }
  ```
- **Respostas**:
  - `201 Created`: Pagamento registrado com sucesso.
  - `500 Internal Server Error`: Erro ao cadastrar pagamento.

### **6. Criar Sinistro**
- **Método**: POST
- **URL**: `http://localhost:5000/sinistros`
- **Body**:
  ```json
  {
    "atendimento_id": 1,
    "tipo_sinistro": "Erro no procedimento",
    "descricao": "Paciente relatou dor intensa após o procedimento.",
    "status": "Em análise"
  }
  ```
- **Respostas**:
  - `201 Created`: Sinistro registrado com sucesso.
  - `500 Internal Server Error`: Erro ao cadastrar sinistro.

## Banco de Dados
A API está conectada a um banco de dados SQL Server hospedado no **Azure**, utilizando as credenciais configuradas no código.

## Tecnologias Utilizadas
- **Python 3.12** + Flask
- **Banco de Dados**: SQL Server (Azure)
- **Docker e Docker Compose**
- **UnixODBC + pyODBC** para conexão com SQL Server

## Link do Vídeo de Apresentação
- [Link do Vídeo](https://youtu.be/Y9_4OHeAdfs)

## Observações
- **Certifique-se de que o banco de dados está rodando** antes de iniciar a API.
- Caso enfrente problemas, utilize os logs dos containers para depuração:
  ```sh
  docker logs api-devops-challenge
  ```

---
🚀 **Projeto desenvolvido para a disciplina de DevOps Tools e Cloud Computing!**

