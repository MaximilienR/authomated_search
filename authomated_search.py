import os
import shutil

# Chemin du dossier où les images seront copiées
dossier_images = "saved_images"

# Création du dossier si il n'existe pas
if not os.path.exists(dossier_images):
    os.makedirs(dossier_images)

# Demande à l'utilisateur de saisir le chemin du dossier spécifique
dossier_specifique = input("Entrez le chemin du dossier spécifique  ou si vous ne connaissez pas tapez random  ")

# Recherche des images dans le dossier spécifique
if os.path.exists(dossier_specifique):
    for root, dirs, files in os.walk(dossier_specifique):
        for file in files:
            # Vérification si le fichier est une image
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                # Copie du fichier image dans le dossier
                shutil.copy2(os.path.join(root, file), dossier_images)

# Si le dossier spécifique n'existe pas ou si il ne contient pas d'images, recherche les images dans tout le système de fichiers
if not os.listdir(dossier_images):
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        for file in files:
            # Vérification si le fichier est une image
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                # Copie du fichier image dans le dossier
                shutil.copy2(os.path.join(root, file), dossier_images)

print("Tous les fichiers images ont été copiés dans le dossier 'Photos'")
input("Appuyez sur une touche pour fermer le script...")