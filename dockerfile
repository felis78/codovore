# Image de base Debian
FROM ubuntu:jammy

# Installer les utilitaires
RUN apt-get update && apt-get install -y \
    curl \
    software-properties-common \
    python3 \
    python3-pip \
    python3-wheel \
    python3-dev \
    python3-venv \
    wget \
    mariadb-client \
    mariadb-server \
    libmariadbclient-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    libmariadb3

# Ajout du dépôt MariaDB et installation de MariaDB
RUN curl -sS https://downloads.mariadb.org/mariadb/repositories/debian/bullseye/mariadb-10.6/bullseye/mariadb_10.6.7-1_bullseye_amd64.deb | dpkg -i -E && \
    apt-get install -fy

# Exposer le port 3306 pour MariaDB
EXPOSE 3306

# Définir le répertoire de travail
WORKDIR /app

# Volume pour la persistance des données
VOLUME [ "/backend"]

# Commande par défaut pour démarrer le conteneur
CMD ["python3", "-m", "venv", ".venv"]
