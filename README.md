# Chiffrement et déchiffrement affine

Ce script Python implémente les fonctions nécessaires pour chiffrer et déchiffrer un texte en utilisant un chiffrement affine.

## Fonction `euclide_etendu(a, b)`

Cette fonction calcule le plus grand commun diviseur (PGCD) de deux nombres `a` et `b` en utilisant l'algorithme d'Euclide étendu. Elle retourne un tuple `(g, x, y)` tel que `g` est le PGCD de `a` et `b`, et `x` et `y` sont les coefficients permettant d'écrire le PGCD comme une combinaison linéaire de `a` et `b`.

## Fonction `inverse_modulaire(a, m)`

Cette fonction utilise l'algorithme d'Euclide étendu pour calculer l'inverse modulaire de `a` modulo `m`. Si l'inverse modulaire n'existe pas (c'est-à-dire si `a` et `m` ne sont pas premiers entre eux), une exception est levée.

## Fonction `chiffrer_texte(plain_text, a, b, m)`

Cette fonction prend un texte clair `plain_text` et chiffre chaque caractère alphabétique en utilisant une transformation affine définie par les paramètres `a` (coefficient multiplicatif), `b` (terme constant), et `m` (taille de l'alphabet). Les caractères non alphabétiques sont laissés inchangés.

## Fonction `dechiffrer_texte(texte_chiffre, a, b, m)`

Cette fonction prend un texte chiffré `texte_chiffre` et le déchiffre en utilisant l'inverse modulaire. Elle utilise les mêmes paramètres que la fonction de chiffrement.

## Exemple d'utilisation

Le script prend en entrée un texte clair, chiffre le texte à l'aide de la transformation affine, puis déchiffre le texte chiffré pour retrouver le texte d'origine.

```python
texte_clair = input("Entrez le texte à chiffrer : ")
a = 5
b = 8
m = 26
```
```python
texte_chiffre = chiffrer_texte(texte_clair, a, b, m)
print(f"Texte chiffré : {texte_chiffre}")

texte_dechiffre = dechiffrer_texte(texte_chiffre, a, b, m)
print(f"Texte déchiffré : {texte_dechiffre}")
```





