# This is a python file I use to quickly create directories for my notes such that I don't need to do mkdir and touch repeatedly
import os
import sys
import shutil

def create_structure(subject, lecture_name):
    subject_dir = os.path.join(os.getcwd(), subject)

    if not os.path.exists(subject_dir):
        os.makedirs(subject_dir)
        print(f"Created directory: {subject_dir}")

    lecture_dir = os.path.join(subject_dir, lecture_name)

    if not os.path.exists(lecture_dir):
        os.makedirs(lecture_dir)
        print(f"Created directory: {lecture_dir}")

    tex_file = os.path.join(lecture_dir, "doc.tex")

    template_file = os.path.join(os.getcwd(), "template.tex")

    if not os.path.exists(template_file):
        print("Error: template.tex not found in the root directory.")
        return

    if not os.path.exists(tex_file):
        shutil.copy(template_file, tex_file)
        print(f"Created file: {tex_file} using {template_file}")
        os.system(f"kitty --detach nvim {tex_file}")
    else:
        print(f"File already exists: {tex_file}")

if len(sys.argv) != 3:
    print("Usage: python create.py Subject LectureName")
else:
    subject = sys.argv[1]
    lecture_name = sys.argv[2]
    create_structure(subject, lecture_name)
