from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os

# Fonction pour générer une paire de clés RSA de 2048 bits
def generer_cles_rsa():
    key = RSA.generate(2048)  # Taille de la clé fixée à 2048 bits
    cle_privee = key.export_key()
    cle_publique = key.publickey().export_key()
    return cle_privee, cle_publique

# Fonction pour charger les clés RSA depuis des fichiers PEM
def charger_cles_rsa():
    if not (os.path.exists("cle_privee.pem") and os.path.exists("cle_publique.pem")):
        print("Les fichiers de clés n'existent pas.")
        return None, None
    
    with open("cle_privee.pem", "rb") as f:
        cle_privee = RSA.import_key(f.read())
    
    with open("cle_publique.pem", "rb") as f:
        cle_publique = RSA.import_key(f.read())
    
    return cle_privee, cle_publique

# Fonction pour chiffrer un fichier avec AES et la clé publique RSA
def crypter_fichier(nom_fichier, cle_publique):
    # Générer une clé AES aléatoire de 256 bits (32 bytes)
    cle_aes = get_random_bytes(32)
    cipher_aes = AES.new(cle_aes, AES.MODE_EAX)

    # Chiffrer le fichier avec AES
    with open(nom_fichier, "rb") as f:
        contenu = f.read()
        ciphertext, tag = cipher_aes.encrypt_and_digest(contenu)

    # Chiffrer la clé AES avec RSA
    cipher_rsa = PKCS1_OAEP.new(cle_publique)
    cle_aes_chiffree = cipher_rsa.encrypt(cle_aes)

    # Écrire le fichier crypté avec la clé AES chiffrée et les données chiffrées
    nom_fichier_crypte = nom_fichier + ".crypte"
    with open(nom_fichier_crypte, "wb") as f:
        f.write(cipher_aes.nonce)
        f.write(tag)
        f.write(cle_aes_chiffree)
        f.write(ciphertext)

    print(f"Le fichier {nom_fichier} a été correctement crypté avec succès.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Générer une nouvelle paire de clés RSA si elles n'existent pas déjà
    if not (os.path.exists("cle_privee.pem") and os.path.exists("cle_publique.pem")):
        print("Génération de nouvelles clés RSA...")
        cle_privee, cle_publique = generer_cles_rsa()
        # Sauvegarder les clés dans des fichiers PEM
        with open("cle_privee.pem", "wb") as f:
            f.write(cle_privee)
        with open("cle_publique.pem", "wb") as f:
            f.write(cle_publique)
        print("Clés RSA générées et sauvegardées.")
    else:
        # Charger les clés RSA existantes depuis les fichiers PEM
        cle_privee, cle_publique = charger_cles_rsa()

    # Nom du fichier à crypter
    fichier_a_crypter = "image.jpg"

    # Crypter le fichier avec la clé publique RSA de 8192 bits
    crypter_fichier(fichier_a_crypter, cle_publique)
