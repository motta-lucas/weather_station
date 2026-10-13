
FROM python:3.11.12-slim

WORKDIR /app

# Instala o uv
COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/

# Copia os arquivos de dependências
COPY pyproject.toml uv.lock README.md ./

# Instala as dependências do projeto
RUN uv sync --locked --no-dev --no-install-project

# Copia o código da aplicação
COPY . .

# Ativa o ambiente virtual criado pelo uv
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]