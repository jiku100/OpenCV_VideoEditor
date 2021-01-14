import tkinter as tk
import tkinter as ttk
from Widgets import *
from PIL import Image, ImageTk



mainWindow = tk.Tk()
ImageButton = ImageButtonFactory(mainWindow, imagesPath= ["./src/save.png", "tiger.jpg"], texts = ["파일 열기", "호랑이"])
ImageButton.grid(column = 0, row = 0, sticky = 'W')
mainWindow.mainloop()