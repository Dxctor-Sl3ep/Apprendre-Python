# Indices — challenge calculatrice

Ces indices donnent une direction sans fournir la solution complète. Essaie
chaque étape seul avant de révéler l'indice suivant.

## Étape 1

Commence par deux variables numériques. Teste chaque opérateur séparément et
compare les résultats avec un calcul fait à la main.

## Étapes 2 et 3

La fonction `input()` renvoie du texte. Réfléchis au type attendu par les
opérations mathématiques et convertis la saisie au bon moment.

## Étape 4

Cherche comment formater un nombre avec deux chiffres après la virgule.
Le formatage de l'affichage ne doit pas forcément modifier la valeur utilisée
pour les calculs.

## Étapes 5 et 6

Les chaînes formatées permettent d'insérer des variables dans un message.
Construis d'abord le message avec les valeurs de `x`, `y`, de l'opérateur et du
résultat.

## Étape 7

Entoure uniquement les instructions qui peuvent échouer. Pour la division,
réfléchis au cas particulier avant d'effectuer le calcul. Un message d'erreur
doit expliquer à l'utilisateur comment corriger sa saisie.

## Étape 8

Une fonction peut recevoir des données, effectuer une tâche précise et
retourner un résultat. Essaie de séparer :

1. la lecture des nombres ;
2. le choix de l'opération ;
3. le calcul ;
4. l'affichage.

## Boss final

Une boucle `while` peut relancer le programme. Ajoute une condition de sortie
explicite et vérifie que les erreurs d'un calcul ne bloquent pas les suivants.

## Bonus

Avant de réduire le nombre de lignes, fais fonctionner une version claire.
Une expression conditionnelle ou une table associant un opérateur à une
fonction peut éviter de répéter plusieurs blocs similaires.

## Questions à se poser

- Que se passe-t-il si l'utilisateur saisit `0` comme diviseur ?
- Que se passe-t-il si l'utilisateur saisit `bonjour` ?
- Que doit faire le programme si l'opérateur vaut `%` ?
- Peut-on tester le calcul sans passer par `input()` ?
