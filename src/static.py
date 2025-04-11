import os 
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    try:
        shutil.copytree(source_dir_path, dest_dir_path)
        print(f"Copied files from '{source_dir_path}' to '{dest_dir_path}'")
    except FileExistsError:
        print(f"Destination directory '{dest_dir_path}' already exists. Skipping copy.")
    except Exception as e:
        print(f"Error copying files: {e}")