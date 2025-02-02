import os
import shutil

RAW_DATA_DIR = "../raw_data"
TRAIN_DIR = "../dataset/train"
VALID_DIR = "../dataset/valid"
SPLIT_RATIO = 0.8

os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(VALID_DIR, exist_ok=True)

def split_data(raw_dir, train_dir, valid_dir, split_ratio):
    images = [f for f in os.listdir(raw_dir) if f.endswith(('.jpg', '.png'))]
    train_count = int(len(images) * split_ratio)

    for img in images[:train_count]:
        shutil.copy(os.path.join(raw_dir, img), os.path.join(train_dir, img))

    for img in images[train_count:]:
        shutil.copy(os.path.join(raw_dir, img), os.path.join(valid_dir, img))

if __name__ == "__main__":
    split_data(RAW_DATA_DIR, TRAIN_DIR, VALID_DIR, SPLIT_RATIO)