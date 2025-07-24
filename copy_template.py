import os
import shutil
import sys

def copy_latex_files(target_dir):
    files = ['template.tex', 'preamble.tex']
    
    os.makedirs(target_dir, exist_ok=True)

    for file in files:
        src = os.path.join(os.getcwd(), file)
        dst = os.path.join(target_dir, file)

        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {file} to {target_dir}")
        else:
            print(f"Error: {file} not found in current directory")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python copy_latex_template.py <target_directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    copy_latex_files(target_directory)
