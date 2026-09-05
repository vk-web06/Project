from pathlib import Path
import json
from collections import defaultdict

from PIL import Image
import matplotlib.pyplot as plt


DATA_DIR = Path("data")

# Use the training annotation file
annotation_file = next(DATA_DIR.rglob("train/_annotations.coco.json"))

with open(annotation_file, "r") as file:
    dataset = json.load(file)


# -----------------------------------
# Match category IDs to category names
# -----------------------------------

category_names = {
    category["id"]: category["name"]
    for category in dataset["categories"]
}


# -----------------------------------
# Match image IDs to labels
# -----------------------------------

image_labels = defaultdict(list)

for annotation in dataset["annotations"]:
    image_id = annotation["image_id"]
    category_id = annotation["category_id"]

    image_labels[image_id].append(
        category_names[category_id]
    )


# -----------------------------------
# Find training folder
# -----------------------------------

train_folder = annotation_file.parent


# -----------------------------------
# Display first 6 images
# -----------------------------------

shown = 0

for image_info in dataset["images"]:

    if shown >= 10:
        break

    image_id = image_info["id"]
    filename = image_info["file_name"]

    image_path = train_folder / filename

    if not image_path.exists():
        continue

    image = Image.open(image_path).convert("RGB")

    labels = image_labels[image_id]

    plt.figure()
    plt.imshow(image)
    plt.title("Labels: " + ", ".join(labels))
    plt.axis("off")
    plt.show()

    shown += 1