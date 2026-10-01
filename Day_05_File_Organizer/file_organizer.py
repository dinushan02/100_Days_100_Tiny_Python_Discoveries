"""
Organize files into folders based on their file extensions.
"""

import os
import shutil

source_folder = "downloads"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        if extension:
            folder_name = extension[1:].upper()
            folder_path = os.path.join(source_folder, folder_name)

            os.makedirs(folder_path, exist_ok=True)

            shutil.move(file_path, os.path.join(folder_path, file))

print("Files organized successfully!")