def euclide_etendu(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = euclide_etendu(b % a, a)
        return (g, x - (b // a) * y, y)

def inverse_modulaire(a, m):
    g, x, y = euclide_etendu(a, m)
    if g != 1:
        raise Exception('L\'inverse modulaire n\'existe pas')
    else:
        return x % m

def chiffrer_texte(plain_text, a, b, m):
    texte_chiffre = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                x = ord(char) - ord('A')
                caractere_chiffre = (a * x + b) % m
                texte_chiffre += chr(caractere_chiffre + ord('A'))
            elif char.islower():
                x = ord(char) - ord('a')
                caractere_chiffre = (a * x + b) % m
                texte_chiffre += chr(caractere_chiffre + ord('a'))
        else:
            texte_chiffre += char
    return texte_chiffre

def dechiffrer_texte(texte_chiffre, a, b, m):
    texte_dechiffre = ""
    a_inv = inverse_modulaire(a, m)
    for char in texte_chiffre:
        if char.isalpha():
            if char.isupper():
                y = ord(char) - ord('A')
                caractere_dechiffre = (a_inv * (y - b)) % m
                texte_dechiffre += chr(caractere_dechiffre + ord('A'))
            elif char.islower():
                y = ord(char) - ord('a')
                caractere_dechiffre = (a_inv * (y - b)) % m
                texte_dechiffre += chr(caractere_dechiffre + ord('a'))
        else:
            texte_dechiffre += char
    return texte_dechiffre


texte_clair = input("Entrez le texte à chiffrer : ")
a = 5
b = 8
m = 26

texte_chiffre = chiffrer_texte(texte_clair, a, b, m)
print(f"Texte chiffré : {texte_chiffre}")

texte_dechiffre = dechiffrer_texte(texte_chiffre, a, b, m)
print(f"Texte déchiffré : {texte_dechiffre}")
