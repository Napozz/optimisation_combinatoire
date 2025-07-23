import csv

def lire_affinites(fichier):
    with open(fichier, 'r') as f:
        reader = csv.reader(f)
        lignes = list(reader)
        n = int(lignes[0][0])
        matrice = []
        for ligne in lignes[1:n+1]:
            matrice.append(list(map(int, ligne)))
    return n, matrice

def score_total(ordre, A):
    n = len(ordre)
    score = 0
    for i in range(n):
        a, b = ordre[i], ordre[(i+1)%n]
        score += A[a][b]
    return score

def placement_greedy(n, A):
    non_places = set(range(n))
    ordre = [0]  # commence arbitrairement par personne 0
    non_places.remove(0)
    while non_places:
        last = ordre[-1]
        suivant = max(non_places, key=lambda x: A[last][x])
        ordre.append(suivant)
        non_places.remove(suivant)
    return ordre

def main():
    n, A = lire_affinites('affinites.csv')
    ordre = placement_greedy(n, A)
    score = score_total(ordre, A)
    print(f"Ordre optimal (greedy): {ordre}")
    print(f"Score total: {score}")

if __name__ == "__main__":
    main()
