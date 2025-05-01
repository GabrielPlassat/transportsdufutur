import os
import re
from datetime import datetime

post_dir = "_posts"

for filename in os.listdir(post_dir):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(post_dir, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extraire date et slug à partir du nom de fichier
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)\.md", filename)
    if not match:
        print(f"Nom de fichier inattendu : {filename}")
        continue

    year, month, day, slug = match.groups()
    permalink = f"/{year}/{month}/{slug}.html"

    # Insérer le permalink après le front matter
    new_lines = []
    front_matter_open = False
    inserted = False

    for line in lines:
        if line.strip() == "---":
            if not front_matter_open:
                front_matter_open = True
            elif front_matter_open and not inserted:
                new_lines.append(f"permalink: {permalink}\n")
                inserted = True
        new_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("✅ Tous les permalinks ont été ajoutés.")