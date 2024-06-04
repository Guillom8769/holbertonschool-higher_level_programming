# Utiliser l'image de base Alpine
FROM alpine:latest

# Installer curl
RUN apk add --no-cache curl

# Copier le fichier de configuration dans le conteneur
COPY config.txt /app/config.txt

# Commande par défaut à exécuter lors du démarrage du conteneur
CMD ["sh"]
