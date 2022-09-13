Développez une architecture back-end sécurisée en utilisant Django ORM

![](https://camo.githubusercontent.com/7c691d06ed3e830244e052e43bb63780a25f0be9c7446cd4bea9f638dae92c99/68747470733a2f2f6f6e617465737465706f7572746f692e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f30322f4c6f676f5f6f70656e636c617373726f6f6d735f6f6e617465737465706f7572746f692e6a7067)

# Résumé du projet

L'application Django doit fournir un ensemble d’endpoints sécurisés pour l’API à l'aide du framework Django REST (avec une base de données PostgreSQL) pour permettre les opérations CRUD (créer, lire, mettre à jour et supprimer) appliquées aux divers objets CRM. Vous devrez créer une interface front-end simple à l'aide du site d'administration Django, laquelle permettra aux utilisateurs autorisés de gérer l'application, d'accéder à l'ensemble des modèles et de vérifier la configuration de la base de données. Les exigences et les spécifications des fonctionnalités CRM ont été énoncées dans les exigences techniques Kanban.

# Démarrer le projet

````Bash
git clone https://github.com/Gauthier3090/P9_OpenClassrooms.git p12_gauthier
cd p12_gauthier
````
## Windows

La création d'environnements virtuels est faite en exécutant la commande venv :

````Bash
python -m venv \path\to\new\virtual\venv
````

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

````Bash
.\venv\Scripts\activate.bat
pip install -r requirements.txt
````

Créer un superuser

```Bash
py manage.py create superuser
```

Pour lancer le projet Django :

````Bash
cd .\src
py .\manage.py migrate
py .\manage.py runserver
````

Dans le navigateur de votre choix, se rendre à l'adresse http://127.0.0.1:5000/

## Unix

La création d'environnements virtuels est faite en exécutant la commande venv :

````Bash
python3 -m venv \path\to\new\virtual\venv
````

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

````Bash
source venv/bin/activate
pip install -r requirements.txt
````

Créer un superuser

```Bash
py manage.py create superuser
```

Pour lancer le projet Django :

````Bash
cd .\src
py .\manage.py migrate
py .\manage.py runserver
````

Dans le navigateur de votre choix, se rendre à l'adresse http://127.0.0.1:5000/
