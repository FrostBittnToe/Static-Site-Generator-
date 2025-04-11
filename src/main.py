import os
import shutil
from static import copy_files_recursive
from page import generate_files_recursive

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Build static pages...")
    generate_files_recursive("content", "public", "template.html")

if __name__ == "__main__":
    main()