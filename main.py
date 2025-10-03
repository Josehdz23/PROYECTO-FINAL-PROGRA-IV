import tkinter as tk
from tkinter import messagebox

class AppRecetas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("RECETARIO")
        self.ventana.geometry("1024x720")
        self.ventana.resizable(False, False)

        self.ventana.mainloop()


if __name__ == "__main__":
    AppRecetas()