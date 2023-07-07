import tkinter as tk
import os
import subprocess
import threading
import ctypes

def open_file_explorer():
    os.startfile('C:\\')

def open_calculator():
    subprocess.Popen('calc.exe')

def open_sound_settings():
    os.system('start ms-settings:sound')

def open_user_accounts():
    os.system('control userpasswords2')

def troubleshoot_sound_problems():
    os.system('msdt.exe /id AudioPlaybackDiagnostic')

def open_themes_settings():
    os.system('start ms-settings:themes')

def open_command_prompt_as_admin():
    os.system('powershell -Command "Start-Process cmd -Verb RunAs"')

def open_powershell_as_admin():
    os.system('powershell -Command "Start-Process powershell -Verb RunAs"')

def run_disk_check():
    drive = 'C:'
    command = f'chkdsk {drive} /f /r /x'
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/k {command}", None, 1)

def run_feature_async(command):
    thread = threading.Thread(target=command)
    thread.start()

features = {
    "Open File Explorer": open_file_explorer,
    "Open Calculator": open_calculator,
    "Open Sound Settings": open_sound_settings,
    "Open User Accounts": open_user_accounts,
    "Troubleshoot Sound Problems": troubleshoot_sound_problems,
    "Open Themes Settings": open_themes_settings,
    "Open Command Prompt as Admin": open_command_prompt_as_admin,
    "Open PowerShell as Admin": open_powershell_as_admin,
    "Run Disk Check": run_disk_check
}

root = tk.Tk()
root.title("Windows Features")

for feature, command in features.items():
    button = tk.Button(root, text=feature, command=lambda cmd=command: run_feature_async(cmd))
    button.pack(fill=tk.X)

root.mainloop()
