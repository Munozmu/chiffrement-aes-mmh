# Fonction pour multiplier deux nombres dans le champ de Galois fini GF(2^8)
# cela simule le fonctionnement de galois dans le contexte de AES
def galois_multiply(a, b):
    result = 0
    
    # Itération sur chaque bit de b
    for _ in range(8):
        # Si le bit actuel de b est 1, XOR avec a
        if b & 1:
            result ^= a
        
        # Vérifier si le bit de poids fort de a est 1
        high_bit_set = a & 0x80
        
        # Décalage à gauche de a (multiplication par 2)
        a <<= 1
        
        # Si le bit de poids fort de a était 1, XOR avec le polynôme irréductible
        if high_bit_set:
            a ^= 0x1b  # 0x1b est le polynôme irréductible x^8 + x^4 + x^3 + x + 1
        
        # Décalage à droite de b (division par 2)
        b >>= 1
    
    return result

# Exemple d'utilisation
result = galois_multiply(0x57, 0x83)
print(hex(result))