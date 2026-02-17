# 26_02_2024
# Objectif 1

# LE CODE VA : .vérifie que c’est bien une séquence ADN. .calcule le taux de GC. .la taille de la séquence..

# RESULTAT ----> La taille de la séquence est 2330 nucléotides. Le taux de GC contenu est 50.52%.





# Vérifie si la séquence est une séquence d'ADN valide

def verifier_sequence_adn(sequence):
    nucleotides_valides = {'A', 'T', 'G', 'C'}
    for nucleotide in sequence:
        if nucleotide not in nucleotides_valides:
            return False
    return True


# Calcule le taux de contenu GC dans la séquence

def calculer_taux_gc(sequence):
    gc = 0  
    for nucleotide in sequence:
        if nucleotide == 'G' or nucleotide == 'C':  # Compte le nombre de nucléotides G et C
            gc += 1
    return (gc / len(sequence)) * 100.0  # Convertit le résultat en pourcentage avec une décimale



def main():
    # Entrer une séquence
    #sequence = input("Entrez une séquence d'ADN : \n").upper()     
    fichier = "seq_TD1.txt"
    with open(fichier, 'r') as fasta_file:
        next(fasta_file) # Ignorer le premier ligne
        # Lire les lignes du fichier de chromosome
        lines = fasta_file.readlines()

        # Concaténer les lignes en une seule chaîne en supprimant les sauts de ligne
        sequence = ''.join(line.strip() for line in lines).upper()

        if verifier_sequence_adn(sequence):
            taux_gc = calculer_taux_gc(sequence) # Calcule le taux de GC
            print(f"La taille de la séquence est {len(sequence)} nucléotides.") # Affiche le taux de GC avec deux décimales
            print(f"Le taux de GC contenu est {taux_gc:.2f}%.")
        else:
            print("La séquence n'est pas une séquence ADN valide.")

            
# Lancer l'exécution du programme
if __name__ == "__main__":
    main()
