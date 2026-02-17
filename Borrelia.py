

# Vérifier séquence ADN valide
def verifier_sequence_adn(sequence):
    nucleotides_valides = {'A', 'T', 'G', 'C', 'N', 'R', 'Y', 'K', 'M', 'S', 'W'} # les bases valides 
    for nucleotide in sequence:
        if nucleotide not in nucleotides_valides:
            print(f"Nucléotide invalide : {nucleotide}")
            return False
    return True


# Calculer le taux de GC 
def calculer_taux_gc(sequence):
    nbA = 0
    nbT = 0
    nbG = 0
    nbC = 0
    nbN = 0
    nbR = 0
    nbY = 0
    nbK = 0
    nbM = 0
    nbS = 0
    nbW = 0

    for nucleotide in sequence:
        if nucleotide == "A":
            nbA += 1
        elif nucleotide == "C":
            nbC += 1
        elif nucleotide == "T":
            nbT += 1
        elif nucleotide == "G":
            nbG += 1
        elif nucleotide == "N":
            nbN += 1
        elif nucleotide == "R":
            nbR += 1
        elif nucleotide == "Y":
            nbY += 1
        elif nucleotide == "W":
            nbW += 1
        elif nucleotide == "S":
            nbS += 1
        elif nucleotide == "M":
            nbM += 1
        elif nucleotide == "K":
            nbK += 1

    nb_TOTAL = nbT + nbG + nbA + nbC + nbN + nbR + nbY + nbK + nbM + nbS + nbW # nombre total de nucleotides 
    tauxGC = ((nbG + nbC) / nb_TOTAL)# Convertit le résultat en pourcentage avec une décimale
    return tauxGC


# Calculer le skew GC 
def calculer_skew_gc(sequence):
    skew_gc = 0  # initialiser le variable skew_gc

    nbG = 0  # initialiser le nombre de G à 0
    nbC = 0  # initialiser le nombre de C à 0

    for nucleotide in sequence:
        if nucleotide == "G":
            nbG += 1
        elif nucleotide == "C":
            nbC += 1
    skew_gc=(nbC - nbG) / (nbG + nbC)  # Calcul du skew GC 
    
    return skew_gc


def main():
    # le fichier de la sequence + les deux fichiers de sortie de taux et skew de gc 
    fichier = "C:/Users/Etudiant/OneDrive/Bureau/HELLOOO/Borrelia_burgdorferi_B31_complete_genome.txt"
    fichier_sortie_taux_gc = "C:/Users/Etudiant/OneDrive/Bureau/HELLOOO/sortie_taux_gc.txt"
    fichier_sortie_skew_gc = "C:/Users/Etudiant/OneDrive/Bureau/HELLOOO/sortie_skew_gc.txt"
    sequence = ""  # Initialisation de la variable sequence
    with open(fichier, 'r') as fasta_file, open(fichier_sortie_taux_gc, 'w') as sortie_file_taux_gc, open(fichier_sortie_skew_gc, 'w') as sortie_file_skew_gc: 
        next(fasta_file)  # Ignorer la première ligne
        
        # Pour effacer les lignes vides 
        for line in fasta_file:
            line = line.strip()  # Supprimer les espaces autour de la ligne
            if line:  # Si la ligne n'est pas vide
                sequence += line  # Ajouter la ligne à la séquence

        # Initialisation de la taille_fenêtre et le pas    
        taille_fenêtre= 100000   
        pas= 10000
        
        # Stocker les résultats dans une liste 
        resultats_taux_gc = []
        resultats_skew_gc = []
        
        for x in range(0,len(sequence)-taille_fenêtre+1,pas):
            seq_fenet=sequence[x:x+taille_fenêtre]

            
            if verifier_sequence_adn(seq_fenet):       # Vérifier si la séquence est une séquence ADN valide
                taux_gc = calculer_taux_gc(seq_fenet)  # Calculer le taux de GC
                skew_gc = calculer_skew_gc(seq_fenet)  # Calculer le skew GC
                # Ajouter les résultats à la liste
                resultats_taux_gc.append((x, taux_gc))
                resultats_skew_gc.append((x, skew_gc))
                
            else:
                resultats_taux_gc.append((x, "Non valide"))
                resultats_skew_gc.append((x, "Non valide"))
        
        # Écrire les résultats dans le fichier de sortie pour le taux de GC
        sortie_file_taux_gc.write("Position\tTaux_GC\n")
        for result in resultats_taux_gc:
            sortie_file_taux_gc.write(f"{result[0]}\t{result[1]}\n")
        
        # Écrire les résultats dans le fichier de sortie pour le skew GC
        sortie_file_skew_gc.write("Position\tSkew_GC\n")
        for result in resultats_skew_gc:
            sortie_file_skew_gc.write(f"{result[0]}\t{result[1]}\n")


# Pour exécuter 
if __name__ == "__main__":
    main()

        
