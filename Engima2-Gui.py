import tkinter as tk
from tkinter import filedialog
import os
import shutil
import subprocess

def browse_folder():
    folder_path = filedialog.askdirectory()
    # تنفيذ خطوات إنشاء الصورة في هذا المجلد
    os.chdir(folder_path)
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "-y", "git", "build-essential", "libssl-dev", "libffi-dev", "python-dev", "python-pip"])
    subprocess.run(["git", "clone", "https://github.com/OpenVisionE2/OpenVisionE2.git"])
    os.chdir("OpenVisionE2")
    subprocess.run(["python", "-m", "venv", ".venv"])
    subprocess.run([".venv/bin/activate"])
    subprocess.run(["pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    shutil.copytree('/path/to/base/image', './')
    subprocess.run(["sed", "-i", "s/LANGUAGE=en/LANGUAGE=ar/g", "settings"])
    subprocess.run(["sed", "-i", "s/TIMEZONE=Europe\\/Berlin/TIMEZONE=Asia\\/Dubai/g", "settings"])
    subprocess.run(["make", "image"])
    tk.messagebox.showinfo(title="تم الانتهاء", message="تم إنشاء صورة Enigma2 بنجاح.")

# إنشاء نافذة tkinter
root = tk.Tk()
root.title("إنشاء صورة Enigma2")

# إضافة زر لاختيار المجلد المستهدف لإنشاء الصورة
button = tk.Button(root, text="تحديد المجلد", command=browse_folder)
button.pack(padx=10, pady=10)

# تشغيل النافذة
root.mainloop()
