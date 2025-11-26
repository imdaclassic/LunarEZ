ver = "0.0"
import requests
import tkinter as tk
from tkinter import messagebox
import os
import sys

def get_latest_string():
    url = "https://raw.githubusercontent.com/imdaclassic/LunarEZ/refs/heads/main/latest.txt"
    response = requests.get(url)
    response.raise_for_status()
    return response.text.strip()

print("Checking for updates/new versions")
latestver = get_latest_string()

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def self_update():
    print("Downloading...")
    url = "https://raw.githubusercontent.com/imdaclassic/LunarEZ/refs/heads/main/LunarEZ.py"
    response = requests.get(url)
    response.raise_for_status()
    new_code = response.text

    print("Writing...")
    current_file = os.path.abspath(sys.argv[0])

    with open(current_file, "w", encoding="utf-8") as f:
        f.write(new_code)

    print(f"{current_file} has been updated.")

if latestver != ver:
    print("New update detected!")
    res = messagebox.askyesno("Update Alert", f"There is a new LunarEZ update (V{latestver}). Do you want to download new update automatically?")
    if res:
        self_update()
        
print("No new updates detected.")

clr()
input("Thanks for use LunarEZ!")
