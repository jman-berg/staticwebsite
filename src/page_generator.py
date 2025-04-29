import os
from markdownparser import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")
    with open(from_path) as mdf:
        markdown_contents = mdf.read()
    with open(template_path) as tf:
        html_template = tf.read()
    html_string = markdown_to_html_node(markdown_contents).to_html()
    title = extract_title(markdown_contents)
    html_template_updated = html_template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as html_f:
        html_f.write(html_template_updated)
    

