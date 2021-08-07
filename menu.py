from tkinter import *
from tkinter import ttk, messagebox as msgbox
from Globals import __VERSION__


class Menubar(Menu):
    """
    Menu qui s'affiche à gauche dans l'application tkinter

    Affiche les actions possibles en fonction de MainFrame
    """

    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        # Création des menus déroulants
        self.create_file_menu() # Menu File
        # ajout about
        self.add_command(
            label="About", command=lambda: msgbox.showinfo("About",
                    f"Pyxel art app v{__VERSION__}\nMade by Merlet Raphaël, 2021 \
                    \nSource : https://github.com/Ilade-s/pyxel-art_tk \
                    \nAssets : https://feathericons.com/"))
    
    def create_file_menu(self):
        pass