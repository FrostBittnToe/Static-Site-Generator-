import os
import shutil
import sys
from static import copy_files_recursive
from page import generate_files_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'

    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Build static pages...")
    generate_files_recursive("content", dir_path_docs, "template.html", basepath=basepath)

    for root, _, files in os.walk(dir_path_docs):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                content = content.replace('href="/', f'href="{basepath}')
                content = content.replace('src="/', f'src="{basepath}')
                with open(filepath, 'w') as f:
                    f.write(content)

if __name__ == "__main__":
    main()