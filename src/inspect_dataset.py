from pathlib import Path
import json
from collections import Counter

DATA_DIR = Path("data")

# Find annotation files
annotation_files = list(DATA_DIR.rglob("*.json"))

for annotation_file in annotation_files:

    print("\nReading:", annotation_file)

    with open(annotation_file, "r") as file:
        dataset = json.load(file)

    # Convert category ID into category name
    category_names = {
        category["id"]: category["name"]
        for category in dataset["categories"]
    }

    # Count each class
    counts = Counter()

    for annotation in dataset["annotations"]:
        category_id = annotation["category_id"]
        category_name = category_names[category_id]

        counts[category_name] += 1

    print("\nClass counts:")

    for class_name, count in counts.items():
        print(f"{class_name}: {count}")