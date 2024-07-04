## Installation du systeme:

### Installer mariadb connector/C:
```
$ sudo apt install wget
$ wget https://r.mariadb.com/downloads/mariadb_repo_setup
$ chmod +x mariadb_repo_setup
$ sudo ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6"
$ sudo apt install libmariadb3 libmariadb-dev
```

### Créer l'environnement virtuel:

``` 
$ python3 -m venv .venv    
```

### Installer les paquests pip:

```
$ pip install -r requirements.txt
``` 
