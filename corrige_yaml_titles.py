import os
import re

def corriger_title(title):
    # Nettoyage basique : échappe les guillemets doubles à l’intérieur du titre
    title = title.replace('"', '\\"')
    return f'title: "{title}"'

def corriger_yaml(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()

    if not lignes or lignes[0].strip() != '---':
        return False  # Pas un fichier Jekyll valide

    yaml_end = None
    for i in range(1, len(lignes)):
        if lignes[i].strip() == '---':
            yaml_end = i
            break

    if yaml_end is None:
        return False  # En-tête YAML non terminé

    yaml = lignes[1:yaml_end]
    corps = lignes[yaml_end+1:]

    nouveau_yaml = []
    modifie = False

    for ligne in yaml:
        if ligne.strip().startswith('title:'):
            # On récupère tout ce qui suit "title:"
            match = re.match(r'^title\s*:\s*(.*)', ligne)
            if match:
                titre_brut = match.group(1).strip().strip('"').strip("'")
                nouveau_yaml.append(corriger_title(titre_brut) + '\n')
                modifie = True
            else:
                nouveau_yaml.append(ligne)  # ne modifie pas si pas de match clair
        else:
            nouveau_yaml.append(ligne)

    if modifie:
        with open(fichier, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.writelines(nouveau_yaml)
            f.write('---\n')
            f.writelines(corps)

    return modifie

# Parcours de tous les fichiers du dossier _posts/
dossier = '_posts'
modifies = []

for fichier in os.listdir(dossier):
    if fichier.endswith('.md'):
        chemin = os.path.join(dossier, fichier)
        if corriger_yaml(chemin):
            modifies.append(fichier)

# Résultat
if modifies:
    print("Titres corrigés dans les fichiers suivants :")
    for f in modifies:
        print(f"- {f}")
else:
    print("Aucune correction nécessaire.")