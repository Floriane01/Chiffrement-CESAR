# Fonction de Chiffrement de Vigenère

La fonction `vigenere_chiffrer` prend deux arguments : le texte à chiffrer (`texte_clair`) et la clé de chiffrement (`cle`). La clé est normalisée en majuscules. Chaque lettre du texte est chiffrée en utilisant un décalage déterminé par la lettre correspondante de la clé.

```python
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
```

>La boucle for itère à travers chaque caractère du texte clair.
>
>La condition if char.isalpha(): vérifie si le caractère est une lettre alphabétique.
>
>La clé est normalisée en majuscules avec cle.upper() pour s''assurer que les lettres sont dans la même casse.
>
>La formule (ord(char) - ord('A' ou 'a') + decalage) % 26 + ord('A' ou 'a') calcule la nouvelle position de la lettre après le décalage, en tenant compte du rebouclage à travers l''alphabet.
>
>Les caractères non alphabétiques restent inchangés.

# Fonction de Déchiffrement de Vigenère

La fonction vigenere_dechiffrer déchiffre un texte chiffré en utilisant la même clé de chiffrement.
Elle fonctionne de manière similaire à la fonction de chiffrement, mais elle utilise un décalage négatif pour retrouver le texte d''origine.


```python
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
```

L''utilisation des deux fonctions est illustrée dans l''exemple ci-dessous :

```python
texte = input("Entrez le texte à chiffrer : ")
cle = input("Entrez la clé : ")

texte_chiffre = vigenere_chiffrer(texte, cle)
print(f"Texte chiffré : {texte_chiffre}")

texte_dechiffre = vigenere_dechiffrer(texte_chiffre, cle)
print(f"Texte déchiffré : {texte_dechiffre}")
```

En utilisant cet exemple, l''utilisateur peut voir comment le texte est chiffré et déchiffré à l''aide du chiffrement de Vigenère avec la clé spécifiée.

