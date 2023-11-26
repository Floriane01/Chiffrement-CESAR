# Fonction de Chiffrement César

La fonction chiffrement_cesar prend une chaîne de caractères (texte) et un décalage (decalage) comme arguments. Elle chiffre chaque lettre alphabétique de la chaîne en utilisant le décalage spécifié.

### Chiffrement

```python
def chiffrement_cesar(texte, decalage):
    result = ""
    for caractere in texte:
        if caractere.isalpha():
            code_ascii = ord('A') if caractere.isupper() else ord('a')
            result += chr((ord(caractere) - code_ascii + decalage) % 26 + code_ascii)
        else:
            result += caractere
    return result
```

- La boucle for itère à travers chaque caractère de la chaîne texte.
- La condition if caractere.isalpha(): vérifie si le caractère est une lettre alphabétique.
- La variable code_ascii est définie en fonction de la casse du caractère, pour normaliser le code ASCII.
- La formule `(ord(caractere) - code_ascii + decalage) % 26 + code_ascii` calcule la nouvelle position de la lettre après le décalage, en tenant compte du rebouclage à travers l''alphabet.
- Les caractères non alphabétiques restent inchangés.

### Déchiffrement

```python
def dechiffrement_cesar(texte, decalage):
    return chiffrement_cesar(texte, -decalage)
```

- La fonction dechiffrement_cesar déchiffre un texte chiffré en utilisant la même logique que la fonction de chiffrement, mais avec un décalage négatif.


## Utilisation

L'exemple d'utilisation des deux fonctions est illustré ci-dessous :

```python
texte = input("Ecrivez le texte à crypter : ")
decalage = input("Ecrivez le nombre de décalage : ")
texte_chiffre = chiffrement_cesar(texte, int(decalage))
texte_dechiffre = dechiffrement_cesar(texte_chiffre, int(decalage))

print("Texte original : ", texte)
print("Texte chiffré : ", texte_chiffre)
print("Texte déchiffré : ", texte_dechiffre)
```

En utilisant cet exemple, l'utilisateur peut voir comment le texte est chiffré et déchiffré à l'aide du chiffrement César avec le décalage spécifié.
