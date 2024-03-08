# Utilisation d'une image de base Python
FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers requis dans le conteneur
COPY requirements.txt /app/requirements.txt

# Installation des dépendances Python
RUN pip install -r requirements.txt

COPY . /app

# Commande pour exécuter le microservice
CMD python score.py