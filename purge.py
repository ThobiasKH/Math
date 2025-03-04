# This python script finds and deletes all auxilary latex files created when I use VimtexCompile

import os

extensions = {".aux", ".fdb_latexmk", ".fls", ".log", ".synctex.gz"}

def find_and_delete_latex_files():
    latex_files = []
    for root, _, files in os.walk(os.getcwd()):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                latex_files.append(file_path)
                os.remove(file_path)
    return latex_files

if __name__ == "__main__":
    files = find_and_delete_latex_files()
    if files:
        print("Deleted LaTeX auxiliary files:")
        for file in files:
            print(file)
    else:
        print("No LaTeX auxiliary files found.")
