## QCAD Version 3.26.0

Usage: `qcad.exe [Options] [Files to open]`

- `-allow-multiple-instances`  
  Don't try to avoid multiple instances from running simultaneously.

- `-always-load-scripts`  
  Forces reloading of scripts when they are used. This is mainly useful during script development, to apply changes without restarting QCAD.

- `-app-id [ID]`  
  Set application ID. Multiple instances of the same application (same ID) cannot run simultaneously unless `-allow-multiple-instances` is used.

- `-autostart [script file]`  
  Starts the given script file instead of the default `scripts/autostart.js`. Note that with this option, QCAD is not started but rather the application implemented in the given script.

- `-config [path]`  
  Reads and stores settings in a configuration file at the given location instead of the default location.

- `-debug-action-order`  
  Print action order information in menus.

- `-enable-script-debugger`  
  Enables the script debugger. NOT recommended as this may cause unexpected behavior when using QCAD.

- `-exec [script file] [options]`  
  Executes the given script file directly after starting QCAD. Options after the script file are passed on to the script.

- `-help`  
  Displays this help.

- `-ignore-script-files`  
  Ignore script files on disk. Only load scripts from plugins if applicable.

- `-locale [locale]`  
  Sets the locale to be used (overrides the language set in the preferences). E.g., `-locale de` starts QCAD in German.

- `-no-gui`  
  Don't use GUI. X11: don't connect to X11 server.

- `-no-show`  
  Use but don't display GUI.

- `-filter [filter]`  
  Opens the subsequent file(s) with the explicitly given import filter.

- `-font-substitution A B`  
  Substitute font A with font B.

- `-rescan`  
  Rescan scripts folder for new add-ons.

- `-version`  
  Displays the application version.

- `-enable-xdata`  
  Enables XData (custom properties) support.

- `-quit`  
  Quits QCAD, for example after executing the given script(s).
