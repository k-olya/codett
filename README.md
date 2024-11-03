# VS Code Time Tracker

A minimalist time-tracking python script for windows. Logs 5 minute intervals during which vscode process `Code.exe` was running and you were not afk.

## Install

To install the required packages, run:

```bat
pip install -r requirements.txt
```

## Run

Add the following `codett.vbs` script to the Startup folder:

```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\path\to\your\desired\working\directory"
WshShell.Run """C:\path\to\python.exe"" ""C:\path\to\time_tracker.py""", 0
```

Make sure to replace `C:\path\to\your\desired\working\directory` as well as `C:\path\to\python.exe` and `C:\path\to\time_tracker.py`

## Output

Generates `vscode_time_log.txt` in its working directory.
