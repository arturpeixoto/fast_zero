Claro, aqui está o README.md completo:

```markdown
# FastAPI Project

Este projeto foi desenvolvido utilizando FastAPI, uma moderna e rápida framework para construção de APIs com Python. A seguir, você encontrará informações sobre as tecnologias utilizadas, o passo a passo para rodar a aplicação, como executar os testes e onde encontrar mais informações sobre o desenvolvedor.

## Tecnologias Utilizadas

- **FastAPI**: Framework para criação de APIs com Python.
- **Poetry**: Gerenciador de dependências e ambientes virtuais.
- **Alembic**: Ferramenta de migrações para bancos de dados SQL.
- **SQLAlchemy**: Biblioteca de ORM para interação com bancos de dados SQL.
- **JWT**: Autenticação e autorização utilizando JSON Web Tokens.
- **Ruff**: Ferramenta de linting para código Python.
- **Taskipy**: Facilitador para execução de tasks definidas no `pyproject.toml`.
- **Pydantic**: Validação de dados baseada em tipos para Python.
- **Pytest**: Framework de testes para Python.
- **Docker**: Plataforma de containerização para criação de ambientes isolados.
- **PostgreSQL**: Foi utilizado com `psycopg` como banco de dados da aplicação.
- **Entre outras**.

## Curso

Este projeto foi desenvolvido como parte de um curso gratuito do canal do YouTube do Eduardo Mendes, especialista em Python.

## Passo a Passo para Rodar a API em um ambiente Python

1. **Instalar o Poetry**:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Criar um Ambiente Virtual**:
   ```bash
   poetry shell
   ```

3. **Instalar as Dependências**:
   ```bash
   poetry install
   ```

4. **Executar as Migrações com Alembic**:
   ```bash
   alembic upgrade head
   ```

5. **Rodar o Docker Compose**:
   Na raiz do projeto, execute:
   ```bash
   docker-compose up -d
   ```

## Testes

Para rodar os testes da aplicação, utilize o comando:
```bash
task test
```

## Deploy

A aplicação foi testada em um ambiente de deploy (fly.io) e está funcionando corretamente, embora atualmente não esteja online.

## Contato

Para mais informações ou para entrar em contato, você pode me encontrar nas seguintes redes sociais:

- [GitHub](https://github.com/arturpeixoto)
- [LinkedIn](https://linkedin.com/in/arturpeixoto)

---

Desenvolvido com ❤️ por [Artur Peixoto](https://github.com/arturpeixoto).
```

Esse README.md oferece uma visão geral do projeto, as tecnologias utilizadas, instruções para configuração e execução, bem como informações de contato.