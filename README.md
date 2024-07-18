# Chiffrement et Déchiffrement de Fichiers avec RSA et AES

Ce projet contient deux scripts Python : `encrypt.py` et `decrypt.py` pour chiffrer et déchiffrer des fichiers en utilisant une combinaison de RSA et AES.

## Prérequis

- Python 3.x
- Bibliothèque `pycryptodome`

Vous pouvez installer la bibliothèque requise en exécutant :

pip install pycryptodome


## Fonctionnement

### 1. Génération des clés RSA

Avant de pouvoir chiffrer ou déchiffrer un fichier, vous devez générer une paire de clés RSA. Cela se fait automatiquement lors de la première exécution du script `encrypt.py` si les fichiers de clés (`cle_privee.pem` et `cle_publique.pem`) n'existent pas déjà.

### 2. Chiffrement des fichiers

Pour chiffrer un fichier, exécutez le script `encrypt.py`. Par défaut, il chiffrera un fichier nommé `image.jpg`. Vous pouvez modifier le script pour utiliser un autre fichier en changeant la valeur de la variable `fichier_a_crypter`.



`python encrypt.py` 

Le script effectue les étapes suivantes :

-   Génère une paire de clés RSA si elles n'existent pas.
-   Charge la clé publique RSA.
-   Chiffre le fichier spécifié (`image.jpg`) en utilisant AES.
-   Chiffre la clé AES avec la clé publique RSA.
-   Sauvegarde le fichier chiffré avec l'extension `.crypte`.

### 3. Déchiffrement des fichiers

Pour déchiffrer un fichier, exécutez le script `decrypt.py`. Par défaut, il déchiffrera un fichier nommé `image.jpg.crypte`. Vous pouvez modifier le script pour utiliser un autre fichier en changeant la valeur de la variable `fichier_a_dechiffrer`.


`python decrypt.py` 

Le script effectue les étapes suivantes :

-   Charge la clé privée RSA.
-   Lit le fichier chiffré et extrait les données chiffrées, le nonce, le tag et la clé AES chiffrée.
-   Déchiffre la clé AES avec la clé privée RSA.
-   Utilise la clé AES pour déchiffrer le contenu du fichier.
-   Sauvegarde le contenu déchiffré dans un nouveau fichier sans l'extension `.crypte`.

## Exécution des Scripts

### Chiffrement



`python encrypt.py` 

### Déchiffrement


`python decrypt.py` 

## Auteurs

Ce projet a été créé par Valcke Enguerrand
## License

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.


 ``Vous pouvez copier et coller ce contenu directement dans votre fichier `README.md`.``
