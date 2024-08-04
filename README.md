### 🤖 README: Automatic QCAD Script Executor

### Overview

QCAD File Watcher is a Python script that monitors changes to a specified JavaScript file and automatically re-executes a QCAD executable with the updated script. This can be particularly useful for developers working on QCAD scripts, as it streamlines the testing process by automatically applying changes without manual intervention. 🔄

### Features

- 📂 Monitors changes to a specified JavaScript file.
- ⚙️ Automatically re-executes QCAD with the updated script upon file modification.

#### 1. **Prerequisites:**
   - 🐍 Python 3.x
   - 📦 `watchdog` library (for file system monitoring)
   - 🖥️ QCAD installed and its executable path known

#### 2. **Setup:**
   - Download `Watch-Qcad.py` for QCAD automation.

#### 3. **Install Required Libraries:**
   - Open terminal and install `watchdog`:
     ```bash
     pip install watchdog
     ```

#### 4. **Configuration:**
   - Edit `Watch-Qcad.py`:
     - Set QCAD executable path:
     ```python
       LOCATION_OF_QCAD_exe = "E:\\Program Files\\QCAD\\qcad.exe"
     ```

#### 5. **Usage:**
   - Run script in terminal:
     ```bash
     python Watch-Qcad.py
     ```
   - Enter JavaScript file path when prompted.

#### 6. **Execution:**
   - Monitors changes in JavaScript file.
   - If QCAD doesn't launch automatically, start QCAD manually to apply changes. 🔄⚙️

#### 7. **Stopping:**
   - Exit script with `Ctrl + C`.

#### 8. **Developer Info:**
   - Version: 1.5.0 🚀
   - Developer: Swastik Gupta 👨‍💻
   - GitHub: [https://github.com/swas02](https://github.com/swas02)

### Notes:
- Ensure paths are correct and accessible.
- Customize `Watch-Qcad.py` for specific needs.
- Contact developer for issues or updates.
