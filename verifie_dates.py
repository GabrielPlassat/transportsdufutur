import os
import yaml

path = "_posts"

for filename in os.listdir(path):
    if not filename.endswith(".md"):
        continue

    full_path = os.path.join(path, filename)
    with open(full_path, encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        parts = content.split("---")
        if len(parts) >= 2:
            try:
                front_matter = yaml.safe_load(parts[1])
                if not front_matter or 'date' not in front_matter:
                    print(f"⚠️  Manque la date : {filename}")
            except Exception as e:
                print(f"⚠️  Erreur YAML dans : {filename} ({e})")