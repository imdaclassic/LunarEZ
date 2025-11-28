ver = "0.0"
import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image
import os
import sys
import importlib
import subprocess
import shutil
import webbrowser
import ctypes
from tkinter import font as tkfont
import json

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if os.path.basename(__file__) != "LunarEZ.py":
    res = messagebox.askokcancel("Filename Warning", "LunarEZ filename is not exactly \"LunarEZ.py\", some items wont work if this persists, please rename it back or continue with issues.", icon="error")
    if not res:
        sys.exit(0)

def json_read(filename: str):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def json_write(filename: str, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return

def ensure_customtkinter():
    try:
        importlib.import_module("customtkinter")
        print("customtkinter is already installed.")
    except ImportError:
        print("customtkinter not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter"])
        print("Installation complete. Restarting program...")
        os.execv(sys.executable, [sys.executable, "LunarEZ.py"])
    import customtkinter
    return customtkinter

ctk = ensure_customtkinter()

# Update Start
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
        os.execv(sys.executable, [sys.executable, "LunarEZ.py"])
        
print("No new updates detected.")
# Update End

# Startup Stuff Start
def download_image(url: str, save_path: str) -> None:
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Image saved to {save_path}")
    else:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")

if not os.path.exists("lib"):
    input("Lib folder not found, please make sure LunarEZ.py is in the LunarV2 folder.")

if not os.path.exists("lib/ez_files"):
    os.mkdir("lib/ez_files")

if not os.path.exists("lib/ez_files/config_saves"):
    os.mkdir("lib/ez_files/config_saves")

if not os.path.exists("lib/ez_files/model_saves"):
    os.mkdir("lib/ez_files/model_saves")

if not os.path.exists("lib/ez_files/model_saves/content.json"):
    with open("lib/ez_files/model_saves/content.json", 'w') as file:
        file.write("{}")

if not os.path.exists("lib/ez_files/config_saves/content.json"):
    with open("lib/ez_files/config_saves/content.json", 'w') as file:
        file.write('{"current": "unnamed", "paths": [["unnamed.json", "unnamed"]]}')

print("Downloading Assets... (If not already there)")
if not os.path.exists("lib/ez_files/icon.png"):
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/icon.png", "lib/ez_files/icon.png")
if not os.path.exists("lib/ez_files/icon.ico"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/icon.ico", "lib/ez_files/icon.ico")
if not os.path.exists("lib/ez_files/banner.png"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/banner.png", "lib/ez_files/banner.png")
if not os.path.exists("lib/ez_files/github_icon.png"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/github_icon.png", "lib/ez_files/github_icon.png")
if not os.path.exists("lib/ez_files/youtube_icon.png"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/youtube_icon.png", "lib/ez_files/youtube_icon.png")
if not os.path.exists("lib/ez_files/v2_icon.png"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/v2_icon.png", "lib/ez_files/v2_icon.png")
if not os.path.exists("lib/ez_files/config_text.png"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/config_text.png", "lib/ez_files/config_text.png")
if not os.path.exists("lib/ez_files/model_text.png"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/model_text.png", "lib/ez_files/model_text.png")
if not os.path.exists("lib/ez_files/PressStart2P-Regular.ttf"): 
    download_image("https://raw.githubusercontent.com/imdaclassic/LunarEZ/main/assets/PressStart2P-Regular.ttf", "lib/ez_files/PressStart2P-Regular.ttf")
# Startup Stuff End

clr()

#main stuff
print(f"LunarEZ Running -- Version: {ver}")

root = ctk.CTk()

FONT_PATH = resource_path("lib/ez_files/PressStart2P-Regular.ttf")

myappid = f'classic.LunarEZ.ez.{ver}'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root.iconbitmap("lib/ez_files/icon.ico")
root.title(f"LunarEZ - V{ver}")
root.geometry("300x600")
root.resizable(0,0)

banner_pil = Image.open("lib/ez_files/banner.png")
banner_img = ctk.CTkImage(light_image=banner_pil, size=(300, 100))
banner_label = ctk.CTkLabel(root, image=banner_img, text="")
banner_label.pack(side="top", fill="x")

#Config Frame

config_frame = ctk.CTkFrame(root, width=270,height=270)

config_pil = Image.open("lib/ez_files/config_text.png")
config_img = ctk.CTkImage(light_image=config_pil, size=(130, 50))
config_label = ctk.CTkLabel(config_frame, image=config_img, text="")
config_label.pack(padx=75)

ctk.CTkLabel(config_frame, text="Select using dropdown menu the config you want to use / edit", font=("Helvetica", 8, "bold")).pack()

def config_select(value):
    print("Current config: "+value)
    data = json_read("lib/ez_files/config_saves/content.json")
    data["current"] = value
    json_write("lib/ez_files/config_saves/content.json", data)

config_selection = ctk.CTkOptionMenu(
    config_frame,
    values=["Loading..."], 
    command=config_select
)
config_selection.pack(pady=5)

def Refresh_Configs():
    data = json_read("lib/ez_files/config_saves/content.json")
    data2 = []
    for i in data["paths"]:
        data2.append(i[1])
    config_selection.configure(values=data2)

    config_selection.set(data["current"])
    config_select(data["current"])

Refresh_Configs()

#Config Frame End

#Model Frame

model_frame = ctk.CTkFrame(root)

model_pil = Image.open("lib/ez_files/model_text.png")
model_img = ctk.CTkImage(light_image=model_pil, size=(130, 50))
model_label = ctk.CTkLabel(model_frame, image=model_img, text="")
model_label.pack(padx=75)


#Model Frame End

tut_icon_pil = Image.open("lib/ez_files/youtube_icon.png")
tut_icon_img = ctk.CTkImage(light_image=tut_icon_pil, size=(40, 40))
def tut_on_click():
    webbrowser.open("https://www.youtube.com/@imdaclassic")
tut_image_button = ctk.CTkButton(root, image=tut_icon_img, text="Tutorial", command=tut_on_click, width=100, height=10, fg_color="white", text_color="black", font=("Helvetica", 18, "bold"))

label = tk.Label(root, text="Click on Config/Model\n Switcher to begin", font=("Helvetica", 15, "bold"))

front_frame = ctk.CTkFrame(root)

config_text_pil = Image.open("lib/ez_files/config_text.png")
config_text_img = ctk.CTkImage(light_image=config_text_pil, size=(130, 50))
def config_text_on_click():
    label.pack_forget()
    tut_image_button.pack_forget()
    config_frame.pack(pady=5, padx=5)
    model_frame.pack_forget()
config_text_button = ctk.CTkButton(
    front_frame,
    image=config_text_img,
    text="",
    command=config_text_on_click,
    width=100,
    height=1,
    fg_color="transparent",
    hover_color="#232b2e",
    corner_radius=8
)
config_text_button.grid(row=0, column=0)

model_text_pil = Image.open("lib/ez_files/model_text.png")
model_text_img = ctk.CTkImage(light_image=model_text_pil, size=(130, 50))
def model_text_on_click():
    label.pack_forget()
    tut_image_button.pack_forget()
    config_frame.pack_forget()
    model_frame.pack(pady=5, padx=5)
model_text_button = ctk.CTkButton(
    front_frame,
    image=model_text_img,
    text="",
    command=model_text_on_click,
    width=100,
    height=1,
    fg_color="transparent",
    hover_color="#232b2e",
    corner_radius=8
)
model_text_button.grid(row=0, column=1)

front_frame.pack(side="top")

label.pack(pady=20)
tut_image_button.pack()

i = ctk.CTkFrame(root)
ctk.CTkLabel(i, text="made with <3 by classic (@probablyclassic on discord)", font=("Helvetica", 10, "bold")).pack()

bottom_frame = ctk.CTkFrame(i)

bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=0)
bottom_frame.grid_columnconfigure(2, weight=1)

github_icon_pil = Image.open("lib/ez_files/github_icon.png")
github_icon_img = ctk.CTkImage(light_image=github_icon_pil, size=(40, 40))
def github_on_click():
    webbrowser.open("https://github.com/imdaclassic/LunarEZ")
github_image_button = ctk.CTkButton(bottom_frame, image=github_icon_img, text="", command=github_on_click, width=100, height=10, fg_color="white")
github_image_button.grid(row=1, column=0, pady=5, padx=5)

youtube_icon_pil = Image.open("lib/ez_files/youtube_icon.png")
youtube_icon_img = ctk.CTkImage(light_image=youtube_icon_pil, size=(40, 40))
def youtube_on_click():
    webbrowser.open("https://www.youtube.com/@imdaclassic")
youtube_image_button = ctk.CTkButton(bottom_frame, image=youtube_icon_img, text="", command=youtube_on_click, width=100, height=10, fg_color="white")
youtube_image_button.grid(row=1, column=1, pady=5, padx=5)

v2_icon_pil = Image.open("lib/ez_files/v2_icon.png")
v2_icon_img = ctk.CTkImage(light_image=v2_icon_pil, size=(40, 40))
def v2_on_click():
    webbrowser.open("https://gannonr.com/ref?key=KUV4esxr1FdWlbFbEHboI3Z9l")
v2_image_button = ctk.CTkButton(bottom_frame, image=v2_icon_img, text="", command=v2_on_click, width=100, height=10, fg_color="white")
v2_image_button.grid(row=1, column=2, pady=5, padx=5)

bottom_frame.pack(side="bottom", fill="x",pady=5, padx=5)

i.pack(side="bottom",fill="x")
root.mainloop()
