from os.path import isfile
import sys
import os, shutil
from page_generator import generate_pages_recursive 

base_path = sys.argv[0] or "/"

def copy_static(source_dir=None, destination_dir=None):
    if not source_dir or not destination_dir:
        current_directory = os.getcwd()
        destination_dir = f"{current_directory}/docs"
        source_dir = f"{current_directory}/static"
        shutil.rmtree(destination_dir)
        os.mkdir(destination_dir)
    source_directories = os.listdir(source_dir)
    for item in source_directories:
        source_path = os.path.join(source_dir, item)
        destination_path = os.path.join(destination_dir, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            os.mkdir(destination_path)
            copy_static(source_path, destination_path)

def main():
    copy_static()
    generate_pages_recursive("content", "template.html", "docs", base_path)

if __name__ == "__main__":
    main()
