import os
from markdownparser import markdown_to_html_node, extract_title

def genereate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"now reading {dir_path_content}")
    content_paths = os.listdir(dir_path_content)
    with open(template_path) as tf:
        html_template = tf.read()
    for item in content_paths:
        source_path = os.path.join(dir_path_content, item)
        destination_path = source_path.replace("content", "public")
        if os.path.isfile(source_path) and item.endswith(".md"):
            with open(source_path) as mdf:
                markdown_contents = mdf.read()
            html_string = markdown_to_html_node(markdown_contents).to_html()
            title = extract_title(markdown_contents)
            html_template_updated = html_template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
            with open(destination_path.replace(".md", ".html"), "w") as html_f:
                html_f.write(html_template_updated)
            print(f"saving... {destination_path}")
        else:
            os.mkdir(destination_path)
            print(f"now creating directory: {destination_path}")
            genereate_pages_recursive(source_path, template_path, dest_dir_path)
                  




