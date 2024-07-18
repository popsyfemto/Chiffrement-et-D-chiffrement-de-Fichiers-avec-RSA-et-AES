from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

# Fonction pour charger la clé privée RSA depuis un fichier PEM
def charger_cle_privee_rsa():
    if not os.path.exists("cle_privee.pem"):
        print("Le fichier de clé privée n'existe pas.")
        return None
    
    with open("cle_privee.pem", "rb") as f:
        cle_privee = RSA.import_key(f.read())
    
    return cle_privee

# Fonction pour déchiffrer un fichier avec la clé privée RSA
def decrypter_fichier(nom_fichier_crypte, cle_privee):
    with open(nom_fichier_crypte, "rb") as f:
        # Lire les données du fichier crypté
        nonce = f.read(16)
        tag = f.read(16)
        cle_aes_chiffree = f.read(256)  # Pour une clé RSA 2048 bits, la taille est 128 bytes
        ciphertext = f.read()

    try:
        # Déchiffrer la clé AES avec RSA
        cipher_rsa = PKCS1_OAEP.new(cle_privee)
        cle_aes = cipher_rsa.decrypt(cle_aes_chiffree)

        # Déchiffrer le fichier avec AES
        cipher_aes = AES.new(cle_aes, AES.MODE_EAX, nonce=nonce)
        contenu_dechiffre = cipher_aes.decrypt_and_verify(ciphertext, tag)

        # Écrire le contenu déchiffré dans un nouveau fichier
        nom_fichier_dechiffre = nom_fichier_crypte.rsplit('.', 1)[0]  # Retire l'extension .crypte
        with open(nom_fichier_dechiffre, "wb") as f:
            f.write(contenu_dechiffre)

        print(f"Le fichier {nom_fichier_crypte} a été correctement déchiffré avec succès.")
    except (ValueError, KeyError) as e:
        print(f"Erreur lors du déchiffrement du fichier {nom_fichier_crypte}: {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Charger la clé privée RSA
    cle_privee = charger_cle_privee_rsa()

    if cle_privee:
        # Nom du fichier à déchiffrer
        fichier_a_dechiffrer = "image.jpg.crypte"

        # Déchiffrer le fichier avec la clé privée RSA
        decrypter_fichier(fichier_a_dechiffrer, cle_privee)
