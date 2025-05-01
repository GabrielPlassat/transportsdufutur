import csv
import os
import re
from datetime import datetime

# Crée le dossier _posts s'il n'existe pas
os.makedirs("_posts", exist_ok=True)

# Fonction pour créer un "slug" propre depuis un titre
def slugify(text):
    return re.sub(r'\W+', '-', text.lower()).strip('-')

# Lecture du fichier CSV avec ; comme séparateur
with open("articles.csv", newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        # Vérification de la présence des champs nécessaires
        if 'Title' not in row or 'Content' not in row or 'Date' not in row:
            print(f"⛔ Ligne ignorée (champs manquants) : {row}")
            continue
        if not row['Date'].strip():
            print(f"⛔ Ligne ignorée (date vide) : {row}")
            continue

        title = row['Title'].strip()
        content = row['Content'].strip()
        slug = row.get('Slug') or slugify(title)

        raw_date = row['Date'].strip()
        parsed_date = None
        date_formats = ["%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M", "%d/%m/%Y", "%Y-%m-%d"]

        for fmt in date_formats:
            try:
                parsed_date = datetime.strptime(raw_date, fmt)
                break
            except ValueError:
                continue

        if not parsed_date:
            print(f"⚠️ Format de date non reconnu, ligne ignorée : {raw_date}")
            continue

        date_str = parsed_date.strftime("%Y-%m-%d")

        # Génération du fichier Markdown
        filename = f"_posts/{date_str}-{slug}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"---\n")
            f.write(f"title: \"{title}\"\n")
            f.write(f"date: {date_str}\n")
            f.write(f"layout: post\n")
            f.write(f"---\n\n")
            f.write(content)

print("✅ Conversion terminée.")