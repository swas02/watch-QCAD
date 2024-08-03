# QCAD File Watcher

## Overview

QCAD File Watcher is a Python script that monitors changes to a specified JavaScript file and automatically re-executes a QCAD executable with the updated script. This can be particularly useful for developers working on QCAD scripts, as it streamlines the testing process by automatically applying changes without manual intervention. 🔄

## Features

- 📂 Monitors changes to a specified JavaScript file.
- ⚙️ Automatically re-executes QCAD with the updated script upon file modification.
- ⏲️ Customizable debounce time to prevent multiple triggers from rapid file changes.
- 👨‍💻 Developer information and version display.

## Prerequisites

- 🐍 Python 3.x
- 📦 `watchdog` library (for file system monitoring)
- 🖥️ QCAD installed and its executable path known

## Installation

1. **Clone the repository** (if applicable):

   ```bash
   git clone https://github.com/swas02/watch-QCAD.git
   ```

2. **Install dependencies**:

   Ensure you have the `watchdog` library installed. You can install it using pip:

   ```bash
   pip install watchdog
   ```

## Configuration

1. **Update the QCAD executable path**:

   Open the script file and update the `LOCATION_OF_QCAD_exe` variable to point to your QCAD executable.

   ```python
   LOCATION_OF_QCAD_exe = "E:\\Program Files\\QCAD\\qcad.exe"
   ```

2. **Provide the JavaScript file path**:

   When running the script, you need to provide the path to the JavaScript file you want to monitor.

## Usage

1. **Run the script**:

   ```bash
   python watcher.py <path_to_your_js_file>
   ```

   Replace `<path_to_your_js_file>` with the actual path to the JavaScript file you want to monitor. 📜

2. **Interact with the script**:

   - The script will print developer information and start monitoring the specified file. 🕵️‍♂️
   - If the file is modified, QCAD will automatically re-execute with the updated script. 🔄
   - Press `[Ctrl + C]` to stop the script. ✋

## Example

```bash
python watcher.py "C:\\path\\to\\your\\script.js"
```

This command will start monitoring the `script.js` file located at `C:\path\to\your\`. 🚀

## Troubleshooting

- ❗ If the script reports that the QCAD executable does not exist, make sure the path is correctly specified.
- ❓ Ensure that the JavaScript file path provided exists and is accessible.

## Developer Information

- **Version**: 1.0.0 🚀
- **Developer**: Swastik Gupta 👨‍💻
- **GitHub**: [https://github.com/swas02](https://github.com/swas02)

Feel free to contribute or raise issues if you encounter any problems! 🛠️

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. 📜

---
