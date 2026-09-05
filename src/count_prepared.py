from pathlib import Path

DATA_DIR = Path("prepared_data")

classes = ["pet", "hdpe", "pp", "other"]

for split in ["train", "valid"]:
    print(f"\n{split.upper()}")

    for plastic_class in classes:
        folder = DATA_DIR / split / plastic_class
        images = list(folder.glob("*"))
        print(f"{plastic_class}: {len(images)}")