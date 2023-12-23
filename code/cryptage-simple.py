"""
Exemple de chiffrage avec la librairie Cryptography
Source : https://pypi.org/project/cryptography/
"""

from cryptography.fernet import Fernet

key = Fernet.generate_key() # génération d'une clé 
                            #(on voit que c'est un chiffrement symétrique puisque on ne génère qu'une clé.)
f = Fernet(key)

token = f.encrypt(b"Ceci est le message chiffre et dechiffre") # message à crypter (b pour convertir en bit)
token

f.decrypt(token) # message décripté