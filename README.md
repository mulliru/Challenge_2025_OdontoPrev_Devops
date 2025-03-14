# Challenge DevOps Tools e Cloud Computing - OdontoPrev

## 📌 Integrantes:
- **Murilo Ferreira Ramos** - RM553315
- **Pedro Luiz Prado** - RM553874
- **William Kenzo Hayashi** - RM552659

## 📌 Distribuição de Atividades
A divisão das atividades foi realizada conforme as disciplinas da grade curricular:

- **Murilo**: DevOps Tools, Cloud Computing, Compliance, Quality Assurance e Tests.
- **Pedro**: Mobile Application Development e Advanced Business Development With .NET.
- **William**: Java Advanced, Mastering Relational e Non-Relational Database, Disruptive Architectures IoT, IOB, Generative AI.

## 📌 Cronograma de Tarefas
- [Link do Trello](https://trello.com/invite/b/6701a3ed3d57ce4ab46300fd/ATTI2c7cf38c5ce5cc04465175370f7a3aedF74A7B2D/backlog-odontoprev)

## 📌 Rodagem da Aplicação
### 🖥️ Requisitos:
- Docker e Docker Compose instalados
- Python 3.12
- Banco de Dados SQL Server

### 🔧 Passos para execução:
1. Clone o repositório:
   ```sh
   git clone https://github.com/mulliru/Challenge_2025_OdontoPrev_Devops.git
   cd Challenge_2025_OdontoPrev_Devops/DevOps_Entrega3
   ```
2. Execute os containers do projeto:
   ```sh
   docker-compose up -d --build
   ```
3. Acesse a API no navegador:
   ```
   http://localhost:5000
   ```
4. Utilize ferramentas como Postman ou cURL para testar os endpoints.

## 📌 Endpoints

### Criar Cliente
- **Método**: POST
- **URL**: `http://localhost:5000/clientes`
- **Exemplo de Body**:
```json
{
    "nome": "João da Silva",
    "email": "joao.silva@email.com",
    "cpf": "123.456.789-00",
    "telefone": "(11) 91234-5678"
}
```
- **Respostas**:
  - `201 Created`: Cliente criado com sucesso
  - `400 Bad Request`: Erro nos dados enviados

### Criar Profissional
- **Método**: POST
- **URL**: `http://localhost:5000/profissionais`
- **Exemplo de Body**:
```json
{
    "nome": "Dr. Maria Oliveira",
    "email": "maria.oliveira@email.com",
    "cpf": "987.654.321-00",
    "cro": "12345",
    "especialidade": "Odontologia",
    "telefone": "(11) 99876-5432"
}
```

### Criar Atendimento
- **Método**: POST
- **URL**: `http://localhost:5000/atendimentos`
- **Exemplo de Body**:
```json
{
    "cliente_id": 1,
    "profissional_id": 1,
    "descricao": "Consulta odontológica de rotina",
    "status": "Pendente"
}
```

### Criar Pagamento
- **Método**: POST
- **URL**: `http://localhost:5000/pagamentos`
- **Exemplo de Body**:
```json
{
    "atendimento_id": 1,
    "valor": "150.00",
    "metodo_pagamento": "Cartão de crédito",
    "status": "Pendente"
}
```

### Criar Sinistro
- **Método**: POST
- **URL**: `http://localhost:5000/sinistros`
- **Exemplo de Body**:
```json
{
    "atendimento_id": 1,
    "tipo_sinistro": "Quebra de dente",
    "descricao": "Quebra de dente durante a consulta",
    "status": "Em análise"
}
```

## 📌 Diagrama Relacional
![Diagrama Relacional](Documentos/Relacional.png)

## 📌 Prints de Testes no Postman
![Teste Postman](Documentos/teste_postman.png)

## 📌 Link do Vídeo de Apresentação
- [Apresentação do Projeto](https://youtu.be/Y9_4OHeAdfs)

