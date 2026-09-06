import os
import shutil
from pathlib import Path

print("⚡ Launching ThunderX File Organizer... ⚡")

downloads_path = Path(os.path.expanduser("~")) / "Downloads"

FOLDER_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Applications": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z", ".tar"]
}

files_moved = 0

for file_path in downloads_path.iterdir():
    if file_path.is_file():
        file_extension = file_path.suffix.lower()
        
        for folder_name, extensions in FOLDER_MAPPING.items():
            if file_extension in extensions:
                destination_folder = downloads_path / folder_name
                destination_folder.mkdir(exist_ok=True)
                
                try:
                    shutil.move(str(file_path), str(destination_folder / file_path.name))
                    print(f"Moved: {file_path.name} -> {folder_name}/")
                    files_moved += 1
                except Exception as e:
                    print(f"Could not move {file_path.name}: {e}")

print(f"\n✅ Workflow completed! Total files organized: {files_moved}")
