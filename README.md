# Find_stroke

This Python script searches for all the text files in the current directory and its subdirectories, and copies the files that contain any of the specified keywords related to stroke into a new directory called "stroke_files". The keywords that the script is looking for are: "stroke", "Stroke", "Ischemic","ischemic","Thrombotic","TIA","tia","thrombotic","Embolic","embolic","Hemorrhagic","hemorrhagic","hemorrhage","Hemorrhage".

Here's a breakdown of what the script does:

Import the necessary modules: os and shutil.
Define the current directory as the starting point for the search and specify the keywords to look for.
Create a new directory called "stroke_files" if it does not already exist.
Traverse through all the directories and subdirectories under the starting directory, and for each text file found:
a. Open the file and read its contents.
b. Check if the file's contents contain any of the specified keywords.
c. If the file contains at least one keyword:
i. Create a new subdirectory in the "stroke_files" directory corresponding to the relative path of the file's parent directory.
ii. Copy the file into the newly created subdirectory.
Note that the script uses the "shutil.copy2()" method to copy the files, which preserves the file metadata such as timestamps and permissions.

It is important to make sure that the script is used with caution, especially if you are working with sensitive or confidential files, as it could potentially move or copy files without your knowledge or permission.
