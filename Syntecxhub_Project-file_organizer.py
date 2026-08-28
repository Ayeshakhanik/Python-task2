import os
import shutil
import logging

# Set up simple logging to track operations
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def organize_folder(folder_path, dry_run=False):
    """
    Scans a folder and moves files into subfolders based on their extension.
    If dry_run is True, it previews changes without moving files.
    """
    if not os.path.exists(folder_path):
        print(f"Error: Directory '{folder_path}' does not exist.")
        return

    # Scan all items in the target directory
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip directories
        if os.path.isdir(item_path):
            continue

        # Extract file extension (e.g., .pdf -> PDF)
        _, ext = os.path.splitext(item)
        if not ext:
            category = "No_Extension"
        else:
            category = ext[1:].upper()  # Remove dot and convert to uppercase

        # Create target subfolder path
        target_dir = os.path.join(folder_path, category)
        destination_path = os.path.join(target_dir, item)

        # Handle filename collisions if file already exists in destination
        if os.path.exists(destination_path) and not dry_run:
            base, extension = os.path.splitext(item)
            destination_path = os.path.join(target_dir, f"{base}_copy{extension}")

        # Action: Dry Run vs Actual Move
        if dry_run:
            logging.info(f"[DRY-RUN] Would move: '{item}' -> '{category}/'")
        else:
            # Create subfolder if it doesn't exist
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            # Move file
            shutil.move(item_path, destination_path)
            logging.info(f"Moved: '{item}' -> '{category}/'")

if __name__ == "__main__":
    path_to_organize = input("Enter the full path of the folder to organize: ").strip()
    
    # Simple menu choice
    mode = input("Do you want to run in Dry-Run mode? (y/n): ").strip().lower()
    is_dry_run = mode == 'y'

    organize_folder(path_to_organize, dry_run=is_dry_run)