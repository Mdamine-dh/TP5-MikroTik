# TP5 – MikroTik CHR REST API avec Python

## 1. Présentation du projet

Ce TP a pour objectif de découvrir l'API REST native de MikroTik RouterOS v7 et d'automatiser la configuration du routeur à l'aide de Python.

## 2. Objectifs

- Découvrir l'API REST de MikroTik.
- Lire les adresses IP et les routes.
- Ajouter, modifier et supprimer des adresses IP.
- Configurer des routes statiques.
- Utiliser le principe d'idempotence.
- Sécuriser les identifiants avec un fichier `.env`.

## 3. Environnement de travail

- MikroTik CHR – RouterOS v7
- VMware Workstation
- Windows 11
- Python 3.14
- Bibliothèques : `requests`, `python-dotenv`

## 4. Structure du projet

```text
TP5-MikroTik/
│
├── .env
├── .gitignore
├── test_connection.py
├── crud.py
├── patch_address.py
├── delete_address.py
├── configure_router.py
└── README.md
```

## 5. Installation des dépendances

```bash
python -m pip install requests python-dotenv
```

## 6. Configuration des variables d'environnement

Le fichier `.env` contient les informations de connexion :

```env
DEVICE_HOST=192.168.56.10
DEVICE_USER=api-user
DEVICE_PASSWORD=YOUR_PASSWORD
```

Le fichier `.gitignore` protège les informations sensibles :

```gitignore
.env
__pycache__/
.venv/
```

## 7. Réalisation du TP

### Étape 1 – Préparation du MikroTik

- Configuration des interfaces réseau.
- Activation du service REST.
- Création de l'utilisateur `api-user`.

### Étape 2 – GET : Lecture des adresses IP

Le script `test_connection.py` permet de tester la connexion et de récupérer les adresses IP configurées sur le routeur.

Commande :

```bash
python test_connection.py
```

Résultat : connexion réussie et affichage des adresses IP.

### Étape 3 – PUT : Ajout d'une adresse IP

Le script `crud.py` permet d'ajouter une adresse IP sur l'interface `ether2`.

Adresse ajoutée :

`192.168.20.1/24`

Commande :

```bash
python crud.py
```

Résultat : adresse IP créée avec succès.

### Étape 4 – PATCH et DELETE

**PATCH :** le script `patch_address.py` récupère l'identifiant de l'adresse IP et modifie son commentaire.

Commande :

```bash
python patch_address.py
```

**DELETE :** le script `delete_address.py` récupère l'identifiant et supprime l'adresse IP.

Commande :

```bash
python delete_address.py
```

### Étape 5 – Routage statique

Le script `configure_router.py` permet de :

- Récupérer les routes existantes avec GET.
- Vérifier les routes demandées.
- Ajouter les routes manquantes.
- Éviter les doublons grâce au principe d'idempotence.

Routes configurées :

| Destination | Gateway |
|---|---|
| 10.10.10.0/24 | 192.168.44.2 |
| 172.16.10.0/24 | 192.168.44.2 |

Commande :

```bash
python configure_router.py
```

Résultat : les routes sont ajoutées lors du premier lancement et détectées comme existantes lors du deuxième lancement.

## 8. Conclusion

Ce TP m'a permis de découvrir l'API REST de MikroTik RouterOS v7 et d'utiliser Python pour automatiser plusieurs opérations réseau.

J'ai appris à effectuer des opérations GET, PUT, PATCH et DELETE, ainsi qu'à configurer des routes statiques en utilisant le principe d'idempotence.

J'ai également appris à protéger les informations de connexion avec un fichier `.env`.

**Remarque technique :** pour les créations de ressources REST, ce projet utilise la méthode PUT, conformément au fonctionnement de l'API REST RouterOS v7. La connexion HTTP est utilisée dans ce laboratoire isolé.
