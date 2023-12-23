"""
Exemple d'un chiffrement par flots
"""
def chiffrementFlot(message, cle):
    messageChiffre = ""
    for i in range(len(message)):
        messageChiffre += chr(ord(message[i]) ^ ord(cle[i % len(cle)]))
    return messageChiffre

message_original = "Bonjour"
cle_secrete = "clesecrete"

messageChiffreFlot = chiffrementFlot(message_original, cle_secrete)
print("Message chiffré par flot:", messageChiffreFlot)