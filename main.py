def vigenere_chiffrer(texte_clair, cle):
    texte_chiffre = ""
    cle = cle.upper()
    index_cle = 0

    for char in texte_clair:
        if char.isalpha():
            decalage = ord(cle[index_cle]) - ord('A')
            index_cle = (index_cle + 1) % len(cle)

            if char.isupper():
                char_chiffre = chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
            else:
                char_chiffre = chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))

            texte_chiffre += char_chiffre
        else:
            texte_chiffre += char

    return texte_chiffre

def vigenere_dechiffrer(texte_chiffre, cle):
    texte_dechiffre = ""
    cle = cle.upper()
    index_cle = 0

    for char in texte_chiffre:
        if char.isalpha():
            decalage = ord(cle[index_cle]) - ord('A')
            index_cle = (index_cle + 1) % len(cle)

            if char.isupper():
                char_dechiffre = chr((ord(char) - ord('A') - decalage) % 26 + ord('A'))
            else:
                char_dechiffre = chr((ord(char) - ord('a') - decalage) % 26 + ord('a'))

            texte_dechiffre += char_dechiffre
        else:
            texte_dechiffre += char

    return texte_dechiffre


texte = input("Entrez le texte à chiffrer : ")
cle = input("Entrez la clé : ")

texte_chiffre = vigenere_chiffrer(texte, cle)
print(f"Texte chiffré : {texte_chiffre}")

texte_dechiffre = vigenere_dechiffrer(texte_chiffre, cle)
print(f"Texte déchiffré : {texte_dechiffre}")
