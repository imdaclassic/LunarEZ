ver = "0.1"
import requests
import tkinter as tk
from tkinter import messagebox
import os

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

if latestver != ver:
    print("New update detected!")
    res = messagebox.askyesno("Update Alert", f"There is a new LunarEZ update (V{latestver}). Do you want to download new update automatically?")
    if res:
        input("Downloading...")
print("No new updates detected.")

clr()
input("Thanks for use LunarEZ!")
