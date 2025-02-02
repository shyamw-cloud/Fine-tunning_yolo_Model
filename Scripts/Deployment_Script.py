import shutil

MODEL_PATH = "../models/fine_tuned_model/weights/best.pt"
LOCAL_REPO_DIR = "../models/saved_models"

os.makedirs(LOCAL_REPO_DIR, exist_ok=True)

def save_model_to_local(model_path, repo_dir):
    shutil.copy(model_path, repo_dir)
    print(f"Model saved to {repo_dir}")

if __name__ == "__main__":
    save_model_to_local(MODEL_PATH, LOCAL_REPO_DIR)