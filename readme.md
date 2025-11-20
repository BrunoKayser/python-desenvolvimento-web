
# **Esse projeto foi feito para eu conhecer o funcionamento do python em desenvolvimento web, então criei um exercício simples(conforme enunciado a baixo) do qual pude explorar os conceitos de desenvolvimento web utilizando python. Sobre os frameworks listados abaixos, ficaram de minha esocolha por serem populares.Fique a vontade para sugerir algo que possa ser melhorado, ou mesmo se desafie a fazer ele, ainda mais se python é desconhecido para você 😄**

# 🧠 Exercício: Sistema Bancário Simples com API REST usando Python + FastAPI

# 🎯 Objetivo:  Criar uma API RESTful para criar conta e consultar.

## 📦 Tecnologias sugeridas
- Python 3.8+
- FastAPI: Construção de APIs
- Uvicorn: Servidor WEB
- SQLAlchemy: Banco de dados (conexão ao Postgres)
- Docker: criação de banco de dados
- pytest-mock: Mock de Testes unitátio 
- pytest: Testes unitáris
- mock-alchemy: Teste unitário de repositório
- pydantic: Manipulação de requests e responses

## 📚 Conceitos que você vai praticar:
- Estruturação de APIs REST
- Lógica de negócios (regras de conta, validações)
- Modelagem de dados (usuário, conta)
- Integração de banco de dados com Postgres
- Orientação a objeto

## ✏️ Descrição do exercício

- Você deve criar uma API com os seguintes recursos:

### 🔹 Conta

- POST /contas – Criar conta com usuário
- GET /contas/{numero_conta} – Obter detalhes da conta
```
A conta deve ter
- Saldo
- Exclusão lógica
- Usuário Dono
    - nome
    - cpf ou cnpj
- Usuário que inseriu
- Data de criação
- Usuário que alterou
- Data/hora de atualização
```
### 🧠 Regras de negócio (para praticar lógica):
- Um mesmo usuário pode ter no máximo 2 contas.
- Saldo inicial deve ser 0.
- O número da conta deve ser único

### 🌱 Desafios extras (para quando quiser expandir):
- Usar banco de dados com SQLAlchemy
- Implementar testes automatizados com pytest
- Criar documentação via Swagger (FastAPI já gera por padrão em /docs)

## 🐳 Informações da aplicação
Necessário subir o arquivo docker para geração do banco de dados docker/docker-compose.yaml, utilizando o comando docker-compose up

### 🗄️ Script para criação das tabelas
```
-- Criação da tabela de usuários
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf_cnpj VARCHAR(20) UNIQUE NOT NULL,
    is_ativo BOOLEAN DEFAULT TRUE,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    inserido_por INTEGER,
    alterado_por INTEGER,
    data_alteracao TIMESTAMP,
    CONSTRAINT fk_usuario_inserido_por FOREIGN KEY (inserido_por) REFERENCES usuario (id),
    CONSTRAINT fk_usuario_alterado_por FOREIGN KEY (alterado_por) REFERENCES usuario (id)
);

-- Criação da tabela de contas
CREATE TABLE  conta (
    id SERIAL PRIMARY KEY,
    saldo NUMERIC(15,2) DEFAULT 0.00,
    usuario_dono_id INTEGER NOT NULL,
    is_ativo BOOLEAN DEFAULT TRUE,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    inserido_por INTEGER,
    alterado_por INTEGER,
    data_alteracao TIMESTAMP,
    CONSTRAINT fk_conta_usuario_dono FOREIGN KEY (usuario_dono_id) REFERENCES usuario (id),
    CONSTRAINT fk_conta_inserido_por FOREIGN KEY (inserido_por) REFERENCES usuario (id),
    CONSTRAINT fk_conta_alterado_por FOREIGN KEY (alterado_por) REFERENCES usuario (id)
);
```
