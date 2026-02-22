import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification

# 1. Define the Downloads directory path dynamically (works on Windows/Mac/Linux)
DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')

# 2. Define destination folders and their corresponding file extensions
DEST_DIRS = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

# 3. Helper function to find the appropriate folder for a given extension
def get_dest_dir(ext):
    for folder, extensions in DEST_DIRS.items():
        if ext.lower() in extensions:
            return folder
    return "Others" # Default folder for unclassified files

# Create the destination directories if they do not exist
for dir_name in DEST_DIRS.keys():
    os.makedirs(os.path.join(DOWNLOADS_DIR, dir_name), exist_ok=True)
os.makedirs(os.path.join(DOWNLOADS_DIR, "Others"), exist_ok=True)

# 4. Define the Event Handler to watch for new files
class MoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Ignore directory creation, we only care about files
        if event.is_directory:
            return

        file_path = event.src_path
        filename = os.path.basename(file_path)
        _, ext = os.path.splitext(filename)

        # Wait a brief moment to ensure the file is completely downloaded
        time.sleep(1)

        dest_folder = get_dest_dir(ext)
        dest_path = os.path.join(DOWNLOADS_DIR, dest_folder, filename)

        try:
            # Move the file to its corresponding folder
            shutil.move(file_path, dest_path)
            
            # Send a desktop notification
            notification.notify(
                title="Smart Organizer 🤖",
                message=f"Successfully moved '{filename}' to {dest_folder}",
                app_name="Desktop Organizer",
                timeout=5
            )
            print(f"[SUCCESS] Moved: {filename} -> {dest_folder}")
        except Exception as e:
            print(f"[ERROR] Could not move {filename}: {e}")

# 5. Main execution block to start the observer
if __name__ == "__main__":
    event_handler = MoverHandler()
    observer = Observer()
    
    # Schedule the observer to watch the Downloads directory
    observer.schedule(event_handler, DOWNLOADS_DIR, recursive=False)
    observer.start()
    
    print(f"[*] Tracking your Downloads folder: {DOWNLOADS_DIR} ...")
    print("[*] Press Ctrl+C to stop.")
    
    try:
        # Keep the script running continuously
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        observer.stop()
        print("\n[*] Stopping the organizer...")
    
    observer.join()