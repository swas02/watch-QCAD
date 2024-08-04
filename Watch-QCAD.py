import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Initial settings
LOCATION_OF_QCAD_exe = "E:\\Program Files\\QCAD\\qcad.exe"

# Define essential messages in a dictionary
MESSAGES = {
    'file_nf': "❌ Error: The file '{file_path}' does not exist. Please enter a valid path: ",
    'js_prompt': "📋 Enter the path to the JavaScript file: ",
    'watching': "👁️ Watching for changes in: {file_path}",
    'stopped': "🛑 Stopped watching.",
    'exit': "Press [Ctrl + C] to exit",
    'launching_qcad': "⚠️ Attempting to launch QCAD executable. If you don't see the QCAD screen, please start it manually.",
    'save_js': "💾 Save your JavaScript file to view changes.",
    'qcad_path_prompt': "📂 QCAD executable not found at '{path}'. Please enter the path to QCAD executable: "
}

# Define developer info and related messages
INFO = {
    'ascii_art': """
░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗  ░██████╗░░█████╗░░█████╗░██████╗░
░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║  ██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║░░░██║░░░██║░░╚═╝███████║  ██║██╗██║██║░░╚═╝███████║██║░░██║
░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║  ╚██████╔╝██║░░██╗██╔══██║██║░░██║
░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║  ░╚═██╔═╝░╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░
    """,
    'version': "Version: 1.5.0 🚀",
    'dev_info': "Developer: Swastik Gupta 👨‍💻",
    'github': "https://github.com/swas02"
}

# Define commands and paths in a dictionary
COMMANDS = {
    'qcad_exec': f'"{LOCATION_OF_QCAD_exe}"',
    'run_script': ' -exec "{file_path}" -always-load-scripts'
}

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.last_modified = 0
        self.debounce_time = 1  # seconds

    def on_modified(self, event):
        if event.src_path == self.file_path:
            current_time = time.strftime('%H:%M:%S')
            current_time_seconds = time.time()
            if current_time_seconds - self.last_modified > self.debounce_time:
                self.last_modified = current_time_seconds
                print(f"🔄 {current_time} Re-executing: {self.file_path}")
                command = f'{COMMANDS["qcad_exec"]}{COMMANDS["run_script"].format(file_path=self.file_path)}'
                subprocess.Popen(command)
                print(MESSAGES['exit'])

def print_developer_info():
    """Print developer info, ASCII art, version, etc."""
    info_text = '\n'.join(f"{value}" for key, value in INFO.items())
    print(f"{'=' * 82}\n{info_text}\n{'=' * 82}")

def get_file_path(prompt):
    """Prompt the user to enter a file path and check if it exists."""
    file_path = input(prompt).strip()
    while not os.path.exists(file_path):
        file_path = input(MESSAGES['file_nf'].format(file_path=file_path)).strip()
    return file_path

def ensure_qcad_exe_path():
    """Ensure the QCAD executable path is valid; prompt user if not."""
    global LOCATION_OF_QCAD_exe
    if not os.path.exists(LOCATION_OF_QCAD_exe):
        LOCATION_OF_QCAD_exe = input(MESSAGES['qcad_path_prompt'].format(path=LOCATION_OF_QCAD_exe)).strip()
        while not os.path.exists(LOCATION_OF_QCAD_exe):
            LOCATION_OF_QCAD_exe = input(MESSAGES['qcad_path_prompt'].format(path=LOCATION_OF_QCAD_exe)).strip()

    COMMANDS['qcad_exec'] = f'"{LOCATION_OF_QCAD_exe}"'

def main():
    print_developer_info()
    
    ensure_qcad_exe_path()  # Ensure QCAD executable path is valid

    js_file = get_file_path(MESSAGES['js_prompt'])

    # Set up the observer and handler
    event_handler = ChangeHandler(js_file)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(js_file), recursive=False)
    observer.start()
    print(MESSAGES['watching'].format(file_path=js_file))

    # Notify user before launching QCAD
    print(MESSAGES['launching_qcad'])
    subprocess.Popen(COMMANDS['qcad_exec'], shell=True)

    # Inform user to save their JS file
    print(MESSAGES['save_js'])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(MESSAGES['stopped'])
    observer.join()

if __name__ == "__main__":
    main()
