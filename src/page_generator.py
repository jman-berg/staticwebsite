import os
from markdownparser import markdown_to_html_node, extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    print(f"now reading {dir_path_content}")
    content_paths = os.listdir(dir_path_content)
    with open(template_path) as tf:
        html_template = tf.read()
    for item in content_paths:
        source_path = os.path.join(dir_path_content, item)
        destination_path = source_path.replace("content", "docs")
        if os.path.isfile(source_path) and item.endswith(".md"):
            with open(source_path) as mdf:
                markdown_contents = mdf.read()
            html_string = markdown_to_html_node(markdown_contents).to_html()
            title = extract_title(markdown_contents)
            html_template_updated = html_template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
            html_template_update_href_basepath = html_template_updated.replace('href="/', f'href="{base_path}')
            html_template_update_src_basepath = html_template_update_href_basepath.replace('href"/', f'href="{base_path}')
            with open(destination_path.replace(".md", ".html"), "w") as html_f:
                html_f.write(html_template_update_src_basepath)
            print(f"saving... {destination_path}")
        else:
            os.mkdir(destination_path)
            print(f"now creating directory: {destination_path}")
            generate_pages_recursive(source_path, template_path, dest_dir_path, base_path)
                  




