# Utilisez l'image de base Python 3.9
FROM python:3.9

# Copiez le code de l'application dans le conteneur
COPY . /app
WORKDIR /app

# Installez les exigences (requirements) de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Chargez les données de la Ligue 1 française
# RUN python load_ligue1_teams.py

# Exposez le port 5000 pour l'application
EXPOSE 5000

# Démarrez l'application
CMD ["python", "app.py"]