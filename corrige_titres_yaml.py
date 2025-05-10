import os
import re

dossier = "_posts"

def corrige_titre(titre):
    titre = titre.strip()

    # Enlève les doubles guillemets s’ils encadrent mal le texte
    if titre.startswith('"') and not titre.endswith('"'):
        titre = titre[1:]
    elif titre.endswith('"') and not titre.startswith('"'):
        titre = titre[:-1]

    # Échappe les guillemets doubles à l’intérieur
    titre = titre.replace('"', '\\"')
    return f'title: "{titre}"'

for fichier in os.listdir(dossier):
    if fichier.endswith(".md"):
        chemin = os.path.join(dossier, fichier)
        with open(chemin, encoding="utf-8") as f:
            lignes = f.readlines()

        # Recherche et corrige la ligne "title:"
        for i, ligne in enumerate(lignes):
            if ligne.strip().startswith("title:"):
                # Extrait le contenu du titre
                titre_match = re.match(r'^title:\s*["\']?(.*)["\']?$', ligne.strip())
                if titre_match:
                    titre = titre_match.group(1)
                    lignes[i] = corrige_titre(titre) + "\n"
                break  # On suppose que le title est sur une seule ligne au début

        with open(chemin, "w", encoding="utf-8") as f:
            f.writelines(lignes)

print("✅ Titres YAML corrigés automatiquement.")