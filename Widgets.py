import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageButtonFactory(tk.Frame):
    def __init__(self, master, imagesPath, texts):
        tk.Frame.__init__(self, master)
        self.master = master
        self.texts = texts
        self.images = []
        for i in range(len(imagesPath)):
            img = Image.open(imagesPath[i])
            img = img.resize((100, 100), Image.ANTIALIAS)
            self.images.append(ImageTk.PhotoImage(img))
        self.createImageButton()
    def createImageButton(self):
        for i in range(len(self.images)):
            button = tk.Button(self, text=self.texts[i], image = self.images[i], compound = 'top')
            button.grid(column = 0, row = i, sticky = 'WE')