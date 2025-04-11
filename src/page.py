from block import markdown_to_html_node
import os
from main import basepath

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line.replace("# ",'', 1)
        
    raise Exception("Title not found, is required")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}")
    from_content = ""
    template_content = ""

    with open(from_path, 'r') as from_file:
        from_content = from_file.read()
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    title = extract_title(from_content)
    content_html = markdown_to_html_node(from_content).to_html()

    content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", content_html)

    content = content.replace('href="/', f'href="{basepath}')
    content = content.replcea('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if os.path.exists(dest_dir) == False:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, 'w') as dest_file:
        dest_file.write(content)

def generate_files_recursive(source_dir_path, dest_dir_path, template_file):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            generate_page(from_path, template_file, dest_path.replace(".md", ".html"))
        else:
            generate_files_recursive(from_path, dest_path, template_file)