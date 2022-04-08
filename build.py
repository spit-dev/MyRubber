import subprocess

print("[+] Espere mientras se compila su archivo...")
subprocess.call("pyinstaller --onefile main.py --icon=./icon.ico", shell=True)