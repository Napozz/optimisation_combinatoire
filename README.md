# Modèle Mathématique : Placement autour d'une table en fonction des affinités

## Données

- **N** : nombre total de personnes.
- **A** : matrice d'affinités de dimension \( N \times N \), où chaque élément \( A\_{ij} \in [0,5] \) représente le niveau d'affinité entre la personne \( i \) et la personne \( j \).
- On suppose que \( A*{ij} = A*{ji} \) (symétrie) et \( A\_{ii} = 0 \) (pas d'affinité avec soi-même).

## Objectif

On souhaite placer les personnes autour d'une table circulaire de façon à **maximiser la somme des affinités entre voisins directs**.

## Représentation

- Soit \( P = [P_1, P_2, \dots, P_N] \) une permutation des \( N \) personnes, représentant leur ordre autour de la table.
- La table est circulaire, donc les voisins de \( P*i \) sont \( P*{i-1} \) et \( P\_{i+1} \), avec indices modulo \( N \).

## Fonction à maximiser

On cherche à maximiser la fonction :
\[
\text{Score}(P) = \sum*{i=1}^{N} A*{P*i, P*{(i \mod N) + 1}}
\]

Ce score représente la somme des affinités entre chaque personne et son voisin de droite (en prenant en compte que \( P\_{N+1} = P_1 \)).

## Contraintes

- \( P \) est une permutation de \( \{0, 1, \dots, N-1\} \).
- Toutes les personnes doivent être placées une et une seule fois.

## Problème combinatoire

Ce problème est équivalent à un problème de **maximisation de poids sur un cycle hamiltonien**, ce qui le rend proche du **Problème du voyageur de commerce (TSP)**, sauf que l'objectif est de maximiser les poids (affinités), pas de les minimiser.

## Solutions possibles

- **Recherche exhaustive** (factorielle en complexité).
- **Algorithme glouton** (greedy).
- **Métaheuristiques** :
  - Recuit simulé (Simulated Annealing)
  - Algorithme génétique
  - Recherche tabou, etc.

Ce modèle peut être utilisé pour développer un algorithme de placement optimal ou semi-optimal selon le contexte (nombre de personnes, contraintes de temps, etc.).
