import tkinter as tk
from PIL import Image, ImageTk
import cv2


mainWindow = tk.Tk()
lbl = tk.Label(mainWindow, text = "text", width = 1600, height = 900)
lbl.grid(column = 0, row = 0, sticky = "NW")
mainWindow.mainloop()
