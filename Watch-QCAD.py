import sys
import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# settings
LOCATION_OF_QCAD_exe = "E:\Program Files\QCAD\qcad.exe"
# =========================================


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.last_modified = 0
        self.debounce_time = 1  # seconds

    def on_modified(self, event):
        current_time = time.time()
        if event.src_path == self.file_path:
            if current_time - self.last_modified > self.debounce_time:
                self.last_modified = current_time
                print(f"🔄 {time.strftime('%H:%M:%S')} Re-executing: {self.file_path}")
                subprocess.Popen( f'"{LOCATION_OF_QCAD_exe}" -exec "{sys.argv[1]}" -always-load-scripts')
                print(f"Press [Ctrl + C] to exit")


def print_developer_info():
    """Print developer info, ASCII art, version, etc."""
    ascii_art = """
░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗  ░██████╗░░█████╗░░█████╗░██████╗░
░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║  ██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║░░░██║░░░██║░░╚═╝███████║  ██║██╗██║██║░░╚═╝███████║██║░░██║
░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║  ╚██████╔╝██║░░██╗██╔══██║██║░░██║
░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║  ░╚═██╔═╝░╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░
    """
    version = "Version: 1.0.0 🚀"
    developer_info = "Developer: Swastik Gupta 👨‍💻"
    github = "https://github.com/swas02"

    print("=" * 82)
    print(ascii_art)
    print(version)
    print(developer_info)
    print(github)
    print("=" * 82)  # Just a line for visual separation


def validate_files_and_arguments():
    """Validate QCAD executable, JavaScript file, and command-line arguments."""
    global LOCATION_OF_QCAD_exe

    # Check QCAD executable
    while not os.path.exists(LOCATION_OF_QCAD_exe):
        LOCATION_OF_QCAD_exe = input(
            f"⚠️ Error: '{LOCATION_OF_QCAD_exe}' does not exist. Enter valid path: ").strip()

    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("📋 Usage: python watcher.py <path to JS file>")
        sys.exit(1)

    js_file = sys.argv[1]
    if not os.path.exists(js_file):
        print(f"❌ Error: The file '{js_file}' does not exist.")
        sys.exit(1)

    return js_file


def main():
    print_developer_info()  # Print developer info at the beginning

    js_file = validate_files_and_arguments()

    # Define the command to run (for demonstration purposes, use an example command)


    # Set up the observer and handler
    event_handler = ChangeHandler(js_file)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(
        js_file), recursive=False)
    observer.start()
    print(f"👁️ Watching for changes in: {js_file}")
    subprocess.Popen( f'"{LOCATION_OF_QCAD_exe}"')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Stopped watching.")
    observer.join()


if __name__ == "__main__":
    main()
