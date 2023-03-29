import os
import shutil

dir_name = "."
keyword = ["stroke", "Stroke", "Ischemic","ischemic","Thrombotic","TIA","tia","thrombotic","Embolic","embolic","Hemorrhagic","hemorrhagic","hemorrhage","Hemorrhage"]
new_dir = "stroke_files"

# create a new directory called "stroke_files"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

for root, dirs, files in os.walk(dir_name):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                contents = f.read()
            if any(word in contents for word in keyword):
                folder_name = os.path.join(new_dir, os.path.relpath(root, dir_name))
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                shutil.copy2(os.path.join(root, file), os.path.join(folder_name, file))
