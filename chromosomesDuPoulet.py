# Objectif 2
# chromosomes POULET
# Verification_Taille_Taux de GC


import os

# Vérifier séquence ADN valide
def verifier_sequence_adn(sequence):
    nucleotides_valides = {'A', 'T', 'G', 'C', 'N'}
    for nucleotide in sequence:
        if nucleotide not in nucleotides_valides:
            return False
    return True



# Calculer le taux de GC 
def calculer_taux_gc(sequence):
    gc = 0  
    for nucleotide in sequence:
        if nucleotide == 'G' or nucleotide == 'C':
            gc += 1
    return (gc / len(sequence)) * 100.0



# Analyser le chromosome et enregistrer les résultats
def analyser_chromosome(fichier_chromosome, dossier_sortie):
    # ecrire le nom du fichier de sortie en ajoutant "resultats_" avant le nom du fichier d'entrée
    nom_fichier_sortie = os.path.join(dossier_sortie, f"resultats_{fichier_chromosome[:-4]}.txt") #-4  est fait pour garantir que le nom du fichier de sortie suit le format attendu, avec "resultats_" ajouté au début et ".txt" à la fin.

    # Ouvrir le fichier de sortie en mode écriture
    with open(nom_fichier_sortie, "w") as f_out:
        # Écrire l'en-tête dans le fichier de sortie_Chromosome_Taille (nucléotides)_Taux de GC (%)
        f_out.write("Chromosome\tTaille (nucléotides)\tTaux de GC (%)\n")

        # Ouvrir le fichier de chromosome en mode lecture
        with open(fichier_chromosome, "r") as f_in:
            # Lire les lignes du fichier de chromosome
            lines = f_in.readlines()
            # Concaténer les lignes en une seule chaîne en supprimant les sauts de ligne et en ignorant la première ligne (l'en-tête)
            sequence = ''.join(line.strip() for line in lines[1:]) # strip() supprime les espaces et les caractères de saut de ligne (comme \n) 

        
            if verifier_sequence_adn(sequence):
                taille_chromosome = len(sequence) # taille de la sequence
                taux_gc = calculer_taux_gc(sequence) # taux de GC dans la séquence

                f_out.write(f"{fichier_chromosome}\t{taille_chromosome}\t{taux_gc:.2f}\n")# Écrire les résultats dans le fichier de sortie
            else:
                print(f"La séquence dans {fichier_chromosome} n'est pas une séquence ADN valide.")# Afficher un message si la séquence n'est pas valide


def main():
    # Liste des noms de fichiers
    fichiers_chromosomes = [f"Gallus_chr{i}.txt" for i in range(1, 11)] + ["Gallus_chr15.txt", "Gallus_chr20.txt"]
    # Nom du dossier où enregistrer les fichiers de sortie
    dossier_sortie = "sortie"
    
    # Créer le dossier de sortie s'il n'existe pas
    #if not os.path.exists(dossier_sortie):
       # os.makedirs(dossier_sortie)
    
    # Parcourir chaque fichier de chromosome dans la liste et les analyser
    for fichier_chromosome in fichiers_chromosomes:
        analyser_chromosome(fichier_chromosome, dossier_sortie)

# Pour exécuter 
if __name__ == "__main__":
    main()









# RESULTATS
# Chromosome	Taille (nucléotides)	Taux de GC (%)
#Gallus_chr1.txt       196449156	40.39
#Gallus_chr2.txt       149539284	40.10
#Gallus_chr3.txt       110642502	40.20
#Gallus_chr4.txt	90861225	40.34
#Gallus_chr5.txt	59506338	41.31
#Gallus_chr6.txt	36220557	41.68
#Gallus_chr7.txt	36382834	41.56
#Gallus_chr8.txt 	29578256	42.02
#Gallus_chr9.txt 	23733309	43.21
#Gallus_chr10.txt	20453248	43.64
#Gallus_chr15.txt	12703657	45.62
#Gallus_chr20.txt	14265659	46.15
