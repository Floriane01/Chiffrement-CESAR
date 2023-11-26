def chiffrement_cesar(texte, decalage):
    result = ""
    for caractere in texte:
        if caractere.isalpha():
            code_ascii = ord('A') if caractere.isupper() else ord('a')
            result += chr((ord(caractere) - code_ascii + decalage) % 26 + code_ascii)
        else:
            result += caractere
    return result


def dechiffrement_cesar(texte, decalage):

    return chiffrement_cesar(texte, -decalage)


texte = input("Ecrivez le texte à crypter")
decalage = input("Ecrivez le nombre de décalage")
texte_c = chiffrement_cesar(texte, int(decalage))
texte_dechiffre = dechiffrement_cesar(texte_c, int(decalage))

print("Texte original:", texte)
print("Texte chiffré:", texte_c)
print("Texte déchiffré", texte_dechiffre)