# Cadastro de Centros de Treinamento e Atletas (Projeto em desenvolvimento)

Este projeto é uma aplicação desenvolvida com FastAPI para o cadastro e gerenciamento de centros de treinamento e atletas. Ele permite a criação, leitura, atualização e exclusão de informações tanto para os centros de treinamento quanto para os atletas registrados, oferecendo uma interface RESTful para interações via HTTP.

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e rápido para a construção de APIs com Python.
- **SQLAlchemy**: ORM para interagir com bancos de dados relacionais.
- **Alembic**: Biblioteca para migrações de banco de dados.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.
- **Pydantic**: Para validação de dados.
- **Python-dotenv**: Para carregar variáveis de ambiente a partir de arquivos `.env`.

## Requisitos

Este projeto requer Python 3.8 ou superior. Para instalar as dependências, você pode usar o arquivo `requirements.txt` incluído no repositório.

```bash
pip install -r requirements.txt
```

## Como Rodar o Projeto

### Usando Docker

Este projeto inclui um `docker-compose.yml` para facilitar a configuração do ambiente de desenvolvimento com Docker.

1. Certifique-se de que o [Docker](https://www.docker.com/get-started) está instalado no seu sistema.
2. Clone o repositório:

   ```bash
   git clone https://github.com/diegotavares16/FastAPI_Centros_de_treinamento.git
   ```

3. Navegue até a pasta do projeto:

   ```bash
   cd FastAPI_Centros_de_treinamento
   ```

4. Suba os containers usando Docker Compose:

   ```bash
   docker-compose up --build
   ```

   Isso irá iniciar os seguintes serviços:
   - **PostgreSQL**: Usando a imagem `postgres:11-alpine`, com a base de dados configurada no arquivo `docker-compose.yml`.

5. A aplicação estará disponível em `http://localhost:8000` e o banco de dados estará rodando no `localhost:5432`.

### Usando o Banco de Dados Local

Se preferir rodar a aplicação localmente sem Docker, siga os seguintes passos:

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure o banco de dados PostgreSQL em sua máquina e atualize o arquivo `alembic.ini` com as informações corretas do banco de dados (se necessário).
   
3. Execute o servidor com o Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   A aplicação estará disponível em `http://127.0.0.1:8000`.

### Migrations com Alembic

Para rodar as migrações do banco de dados com Alembic, siga os passos abaixo:

1. Certifique-se de que o banco de dados esteja rodando.
2. Gere as migrações (caso precise):

   ```bash
   alembic revision --autogenerate -m "Descrição da migração"
   ```

3. Aplique as migrações:

   ```bash
   alembic upgrade head
   ```

## Endpoints

### /centros
- **GET /centros**: Retorna a lista de centros de treinamento.
- **POST /centros**: Cria um novo centro de treinamento.
- **PUT /centros/{id}**: Atualiza os dados de um centro de treinamento.
- **DELETE /centros/{id}**: Deleta um centro de treinamento.

### /atletas
- **GET /atletas**: Retorna a lista de atletas.
- **POST /atletas**: Cria um novo atleta.
- **PUT /atletas/{id}**: Atualiza os dados de um atleta.
- **DELETE /atletas/{id}**: Deleta um atleta.

## Contribuição

Sinta-se à vontade para contribuir para o projeto! Para isso, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie uma branch para sua alteração (`git checkout -b feature/nome-da-feature`).
3. Faça as alterações necessárias e adicione testes, se possível.
4. Envie um pull request com uma descrição clara da sua mudança.

