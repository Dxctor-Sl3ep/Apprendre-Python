# Challenge : construire une calculatrice

## Mission

Construire une calculatrice en plusieurs niveaux. Chaque étape doit fonctionner
avant de passer à la suivante. Le but n'est pas seulement d'obtenir le bon
résultat, mais aussi de rendre le programme compréhensible et agréable à utiliser.

## Règles du challenge

- Utiliser deux nombres `x` et `y`.
- Tester chaque opération après l'avoir ajoutée.
- Ne pas copier la solution : utiliser les indices de [hint.md](./hint.md) si nécessaire.
- Conserver un programme exécutable à la fin de chaque étape.

## Étapes

### Étape 1 — Le moteur de calcul

Déclare deux variables avec des valeurs prédéfinies et calcule :

- l'addition 
- la soustraction  
- la multiplication 
- la division 

**Validation :** les quatre résultats sont affichés correctement.

### Étape 2 — Maîtriser les décimales

Affiche les résultats avec au maximum deux chiffres après la virgule.

**Validation :** un résultat comme `5` ne devient pas inutilement `5.00`,
mais un résultat comme `3.14159` est affiché sous la forme `3.14`.

### Étape 3 — Choisir `x`

Remplace la valeur prédéfinie de `x` par une valeur saisie par l'utilisateur.

**Validation :** le programme utilise bien le nombre fourni par l'utilisateur.

### Étape 4 — Choisir `y`

Fais la même chose pour `y`.

**Validation :** l'utilisateur choisit les deux nombres avant le calcul.

### Étape 5 — Améliorer les messages

Remplace les affichages bruts comme `print(z)` par un message compréhensible,
par exemple : `Votre résultat est : z`.

**Validation :** l'utilisateur comprend immédiatement ce qui est affiché.

### Étape 6 — Décrire l'opération

Affiche l'opération complète avec ses valeurs et son résultat :

> Le résultat de `x + y` équivaut à `z`.

**Validation :** le message indique l'opération effectuée et son résultat.

### Étape 7 — Rendre le programme robuste

Prévois les erreurs courantes :

- une saisie qui n'est pas un nombre ;
- une division par zéro ;
- une opération inconnue.

**Validation :** le programme affiche une explication claire au lieu de
s'arrêter brutalement.

### Étape 8 — Passer en clean code

Améliore la structure du programme :

- sépare les responsabilités dans des fonctions ;
- choisis des noms de variables explicites ;
- évite de répéter le même code ;
- garde une indentation et un formatage réguliers.

**Validation :** une autre personne peut lire et modifier le code facilement.

## Boss final — Mode continu

Ajoute une boucle pour permettre plusieurs calculs sans relancer le programme.
Prévois une commande pour quitter proprement la calculatrice.

## Bonus — Défi des 5 lignes

Crée une version fonctionnelle en moins de 5 lignes.

La version courte doit rester lisible et gérer au minimum le choix de
l'opération. Ce bonus est facultatif : la qualité du code reste prioritaire
sur le nombre de lignes.