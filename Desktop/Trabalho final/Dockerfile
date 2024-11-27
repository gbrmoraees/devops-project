# Use uma imagem Python 3.x
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY ./src /app

# Instala as dependências
RUN pip install Flask

# Expõe a porta 8080
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "app.py"]
